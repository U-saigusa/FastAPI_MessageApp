# Pydanticのschema

from datetime import datetime
from pydantic import BaseModel, constr, field_validator

# メッセージの基本的な構造を定義
class MessageBase(BaseModel):
    content: str

# メッセージ作成時の構造を定義。MessageBaseを継承しているためcontentを持つ。
class MessageCreate(MessageBase):
    # pydanticのconstrを使って、contentが空白でないことをチェックする
    # content: constr(min_length=1)

    # メッセージのカスタムバリデーションを行う関数を定義
    @field_validator('content')
    # class内で定義されたメソッドは、第一引数に自分自身を受け取る必要があるが、staticmethodを使うことで第一引数を省略で
    @staticmethod
    def check_content(value):
        if len(value) < 1:
            raise ValueError('メッセージは1文字以上で送信してください')
        if value.strip() == "":
            raise ValueError('空白のメッセージは送信できません')
        return value

# DBから取得したメッセージを返す際の構造を定義。MessageBaseを継承しているためcontentを持つ。
class Message(MessageBase):
    id: int
    created_at: datetime

    # PydanticにSQLAlchemyのオブジェクトを返す際に必要な設定
    class Config:
        orm_mode = True

class MessageUpdate(MessageBase):
    pass