from django.db import models
from django.db.models import Q

class Phone(models.Model):
	phone_number = models.CharField(blank=True, max_length=25)
	active = models.BooleanField(default=True)

	def _messages(self):
		return Message.objects.filter(Q(from_phone=self)|Q(to_phone=self))
	messages = property(_messages)

	def send_sms(self, message):
		from twilio.rest import TwilioRestClient
		from django.conf import settings

		if not self.active:
			return False

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
			m = Message(text=message, to_phone=self)
			m.save()
		return True

	def __unicode__(self):
		return "%s" % (self.phone_number)

class Message(models.Model):
	from_phone = models.ForeignKey(Phone, blank=True, null=True, related_name="from_messages")
	to_phone = models.ForeignKey(Phone, blank=True, null=True, related_name="to_messages")
	text = models.CharField(blank=True, max_length=160)
	sent = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		if self.from_phone:
			return "From %s: %s" % (self.from_phone, self.text)
		if self.to_phone:
			return "To %s: %s" % (self.to_phone, self.text)
		return "%s" % (self.text)