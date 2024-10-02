# FastAPIのエントリーポイント（APIのルート）
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import get_db, engine

models.Base.metadata.create_all(bind=engine)

# FastAPIのインスタンスを生成
app = FastAPI()

# メッセージを取得するエンドポイント
# response_modelはレスポンスの構造を指定する
@app.get("/messages/", response_model=list[schemas.Message])
# DpendesはFastAPIの依存性注入機能を使ってDBセッションを取得する
def read_messages(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    messages = crud.get_messages(db, skip=skip, limit=limit)
    return messages

# メッセージを作成するエンドポイント
@app.post("/messages/", response_model=schemas.Message)
def create_message(message: schemas.MessageCreate, db: Session = Depends(get_db)):
    return crud.create_message(db=db, message=message)


@app.put("/messages/{message_id}", response_model=schemas.Message)
def update_message(id: int, message: schemas.MessageUpdate, db: Session = Depends(get_db)):
    old_message = crud.get_message_by_id(db=db, id=id)
    if old_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return crud.update_message(db=db, new_message=message, id=id)

@app.delete("/messages/{message_id}")
def delete_message(id: int, db: Session = Depends(get_db)):
    old_message = crud.get_message_by_id(db=db, id=id)
    if old_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return crud.delete_message(db=db, id=id)
