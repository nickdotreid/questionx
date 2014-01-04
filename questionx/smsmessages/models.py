from django.db import models

class Phone(models.Model):
	class Meta:
		abstract = True
	phone_number = models.CharField(blank=True, max_length=25)

	def send_sms(self, message):
		from twilio.rest import TwilioRestClient
		from django.conf import settings

		client = False
		
		if settings.TWILIO_ACCOUNT and settings.TWILIO_TOKEN and settings.SMS_FROM_NUMBER:
			account = settings.TWILIO_ACCOUNT
			token = settings.TWILIO_TOKEN
			client = TwilioRestClient(account, token)
		message_length = 140
		messages = []
		m = []
		for line in message.split("\n"):
			if len(m) + len(line) >= message_length:
				messages.append("".join(m))
				m = []
			m.append(line)
		if len(m) > 0:
			messages.append("".join(m))
		num = 0
		for message in messages:
			num += 1
			message_count = '\n('+str(num)+' of '+str(len(messages))+')'
			if len(messages) <= 1:
				message_count = ''
			if client:
				message = client.sms.messages.create(to=self.phone_number, from_=settings.SMS_FROM_NUMBER,
				                                     body=message + message_count)
			elif settings.DEBUG:
				print "To " + self.phone_number + ":: " + message + message_count
		return True

	def __unicode__(self):
		return "Phone Number: %s" % (self.phone_number)