from django.dispatch import receiver

from smsmessages.signals import smsmessage

from smsmessages.models import Message

@receiver(smsmessage)
def save_message(sender, **kwargs):
	phone = kwargs.get("phone")
	message = kwargs.get("message")
	m = Message(from_phone=phone, text=message)
	m.save()

@receiver(smsmessage)
def stop_sending_to_phone(sender, **kwargs):
	phone = kwargs.get("phone")
	message = kwargs.get("message")
	if message == 'stop':
		phone.active = False
		phone.save()