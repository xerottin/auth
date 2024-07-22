from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from . import models, database
from .celery_worker import send_email_task

app = FastAPI()

# Создание всех таблиц в базе данных
models.Base.metadata.create_all(bind=database.engine)


class EmailRequest(BaseModel):
    email: str
    subject: str
    message: str


@app.post("/send-email/")
async def send_email(email_request: EmailRequest, db: Session = Depends(database.get_db)):
    task = send_email_task.delay(email_request.email, email_request.subject, email_request.message)
    email_notification = models.EmailNotification(
        email=email_request.email,
        subject=email_request.subject,
        message=email_request.message
    )
    db.add(email_notification)
    db.commit()
    db.refresh(email_notification)
    return {"task_id": task.id, "email_id": email_notification.id}
