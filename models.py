from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()
metadata = Base.metadata


class EmailNotification(Base):
    __tablename__ = "email_notifications"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    subject = Column(String)
    message = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="Pending")
