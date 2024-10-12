import os
import resend
from typing import List
from abc import ABC, abstractmethod

resend.api_key = os.getenv("EMAIL_RESEND_API_KEY")

class NotificationStrategy(ABC):
    @abstractmethod
    def notify(self, message: str):
        pass

class EmailNotificationStrategy(NotificationStrategy):
    def __init__(self, to_email: List[str], subject: str):
        self.to_email = to_email
        self.subject = subject

    def notify(self, message: str):
        send_email(self.to_email, self.subject, message)

class SMSNotificationStrategy(NotificationStrategy):
    def notify(self, message: str):
        print(f"Sending SMS notification: {message}")

class PushNotificationStrategy(NotificationStrategy):
    def notify(self, message: str):
        print(f"Sending push notification: {message}")

def send_email(to_email: List[str], subject: str, html: str) -> dict:
    send: dict = resend.Emails.send(
        {
            "from": os.getenv("EMAIL_FROM"),
            "to": to_email,
            "subject": subject,
            "html": html,
        }
    )
    return send
