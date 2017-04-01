#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from django.conf import settings
from django.http import HttpResponse
from django.template import loader
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from integrations.core.views import MailgunGenericContactView


class FinaceroContactView(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.FINACERO_MAILGUN_DOMAIN
    RECIPIENT = settings.FINACERO_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/generic_contact.html'
    FROM_TEXT = 'Finacero'


class RochaLanderosContactView(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.ROCHA_LANDEROS_MAILGUN_DOMAIN
    RECIPIENT = settings.ROCHA_LANDEROS_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/generic_contact.html'
    FROM_TEXT = 'Rocha Landeros'


class WorkingLabsContactView(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.WORKING_LABS_MAILGUN_DOMAIN
    RECIPIENT = settings.WORKING_LABS_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/generic_contact.html'
    FROM_TEXT = 'Working Labs'

