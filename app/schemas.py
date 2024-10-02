# Pydanticのschema

from datetime import datetime
from pydantic import BaseModel

# メッセージの基本的な構造を定義
class MessageBase(BaseModel):
    content: str

# メッセージ作成時の構造を定義。MessageBaseを継承しているためcontentを持つ。
class MessageCreate(MessageBase):
    pass

# DBから取得したメッセージを返す際の構造を定義。MessageBaseを継承しているためcontentを持つ。
class Message(MessageBase):
    id: int
    created_at: datetime

    # PydanticにSQLAlchemyのオブジェクトを返す際に必要な設定
    class Config:
        orm_mode = True

class MessageUpdate(MessageBase):
    pass