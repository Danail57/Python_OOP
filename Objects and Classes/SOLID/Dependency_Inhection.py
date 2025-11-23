from abc import ABC, abstractmethod


class MessageService(ABC):
    @abstractmethod
    def send_message(self):
        pass


class Email(MessageService):
    def send_message(self):
        print("Sending email...")


class SMS(MessageService):
    def send_message(self):
        print("Sending SMS...")


class Notification:
    def __init__(self, service: MessageService):
        self._service = service

    def promotional_notification(self):
        self._service.send_message()
email_service = Email()
sms_service = SMS()

email_notification = Notification(email_service)
sms_notification = Notification(sms_service)

email_notification.promotional_notification()
sms_notification.promotional_notification()
