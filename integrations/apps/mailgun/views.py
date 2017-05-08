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
    SUBJECT = 'Nuevo contacto desde pagina web'


class RochaLanderoContactView(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.ROCHA_LANDERO_MAILGUN_DOMAIN
    RECIPIENT = settings.ROCHA_LANDERO_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/generic_contact.html'
    FROM_TEXT = 'Rocha Landero'
    SUBJECT = 'Nuevo contacto desde pagina web'


class RochaLanderoCarrerView(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.ROCHA_LANDERO_MAILGUN_DOMAIN
    RECIPIENT = settings.ROCHA_LANDERO_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/rocha_landeros_carrers.html'
    FROM_TEXT = 'Rocha Landero'
    SUBJECT = 'Nuevo contacto desde Careers'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(RochaLanderoCarrerView, self) \
            .dispatch(request, *args, **kwargs)

    def post(self, request):
        ctx = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
            'birthday': request.POST.get('birthday'),
            'master': request.POST.get('master'),
            'languages': request.POST.get('languages'),
        }

        body = loader.render_to_string(self.EMAIL_TEMPLATE, ctx)

        endpoint = 'https://api.mailgun.net/v3/{0}/messages'.format(self.DOMAIN)
        response = requests.post(
            endpoint, auth=('api', self.KEY), data={
                'from': '{0} <postmaster@{1}>'.format(self.FROM_TEXT, self.DOMAIN),
                'to': self.RECIPIENT,
                'subject': self.SUBJECT,
                'html': body
            })

        if response.status_code != 200:
            value = '0'
        else:
            value = '1'

        return HttpResponse(value)


class WorkingLabsContactView(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.WORKING_LABS_MAILGUN_DOMAIN
    RECIPIENT = settings.WORKING_LABS_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/generic_contact.html'
    FROM_TEXT = 'Working Labs'
    SUBJECT = 'Nuevo contacto desde pagina web'


class WorkingLabsFreeDayView(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.WORKING_LABS_MAILGUN_DOMAIN
    RECIPIENT = settings.WORKING_LABS_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/generic_contact.html'
    FROM_TEXT = 'Working Labs'
    SUBJECT = 'Nuevo contacto de 21 free day pass'


class WorkingLabsPartnershipView(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.WORKING_LABS_MAILGUN_DOMAIN
    RECIPIENT = settings.WORKING_LABS_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/working_labs_partner.html'
    FROM_TEXT = 'Working Labs'
    SUBJECT = 'Nueva contacto de partnership'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(WorkingLabsPartnershipView, self) \
            .dispatch(request, *args, **kwargs)

    def post(self, request):
        ctx = {
            'name': request.POST.get('name'),
            'last_name': request.POST.get('last_name'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
            'client_name': request.POST.get('client_name'),
            'client_email': request.POST.get('client_email'),
            'client_phone': request.POST.get('client_phone'),
            'client_company': request.POST.get('client_company'),
        }

        body = loader.render_to_string(self.EMAIL_TEMPLATE, ctx)

        endpoint = 'https://api.mailgun.net/v3/{0}/messages'.format(self.DOMAIN)
        response = requests.post(
            endpoint, auth=('api', self.KEY), data={
                'from': '{0} <postmaster@{1}>'.format(self.FROM_TEXT, self.DOMAIN),
                'to': self.RECIPIENT,
                'subject': self.SUBJECT,
                'html': body
            })

        if response.status_code != 200:
            value = '0'
        else:
            value = '1'

        return HttpResponse(value)

