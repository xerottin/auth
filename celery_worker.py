from celery import Celery
from sqlalchemy.orm import Session

from database import SessionLocal
from models import EmailNotification

celery = Celery(
    'worker',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)


@celery.task
def send_email_task(email: str, subject: str, message: str):
    db: Session = SessionLocal()
    try:
        print(f"Отправка email: {email}, Тема: {subject}, Сообщение: {message}")

        email_notification = db.query(EmailNotification).filter_by(email=email).first()
        if email_notification:
            email_notification.status = "Sent"
            db.commit()
            db.refresh(email_notification)
    finally:
        db.close()

    return {"status": "Email sent successfully"}
