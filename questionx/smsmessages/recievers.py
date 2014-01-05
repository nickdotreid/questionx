from django.dispatch import receiver

from smsmessages.signals import smsmessage

@receiver(smsmessage)
def stop_sending_to_phone(sender, **kwargs):
	phone = kwargs.get("phone")
	message = kwargs.get("message")
	if message == 'stop':
		phone.active = False
		phone.save()