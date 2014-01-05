import django.dispatch

smsmessage = django.dispatch.Signal(providing_args=["phone","message"])