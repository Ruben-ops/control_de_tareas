from app.notification_strategy import NotificationStrategy, EmailNotificationStrategy, SMSNotificationStrategy, PushNotificationStrategy

class NotificationService:
    def __init__(self, strategy: NotificationStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: NotificationStrategy):
        self._strategy = strategy

    def notify(self, message: str):
        self._strategy.notify(message)
