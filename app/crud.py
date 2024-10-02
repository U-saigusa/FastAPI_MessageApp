# CRUD操作を定義

from sqlalchemy.orm import Session
from . import models, schemas

# メッセージを取得
# skip: 何件目から取得するか
# limit: 何件取得するか
# db: Session のコロン以降は型ヒント（アノテーション）
def get_messages(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Message).offset(skip).limit(limit).all()

# メッセージをIDで取得
def get_message_by_id(db: Session, id: int):
    return db.query(models.Message).filter(models.Message.id == id).first()

# メッセージを作成
def create_message(db: Session, message: schemas.MessageCreate):
    db_message = models.Message(content=message.content)
    db.add(db_message)
    db.commit()
    # 自動生成される値（ID、created_at）を取得するためにリフレッシュ
    db.refresh(db_message)
    return db_message

def update_message(db: Session, new_message: schemas.MessageUpdate, id: int):
    db_message = db.query(models.Message).filter(models.Message.id == id).first()
    db_message.content = new_message.content
    db.commit()
    db.refresh(db_message)
    return db_message

def delete_message(db: Session, id: int):
    db_message = db.query(models.Message).filter(models.Message.id == id).first()
    db.delete(db_message)
    db.commit()
    return "delete complete"