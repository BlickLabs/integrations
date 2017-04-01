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


class FinaceroContactView(View):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.FINACERO_MAILGUN_DOMAIN
    RECIPIENT = settings.FINACERO_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/finacero_contact.html'
    FROM_TEXT = 'Finacero'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(FinaceroContactView, self) \
            .dispatch(request, *args, **kwargs)

    def post(self, request):
        key = self.KEY
        domain = self.DOMAIN
        recipient = self.RECIPIENT

        ctx = {
            'name': request.POST.get('name'),
            'last_name': request.POST.get('last_name'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
            'company': request.POST.get('company'),
            'message': request.POST.get('message'),
        }

        body = loader.render_to_string(self.EMAIL_TEMPLATE, ctx)

        endpoint = 'https://api.mailgun.net/v3/{0}/messages'.format(domain)
        response = requests.post(
            endpoint, auth=('api', key), data={
                'from': '{0} <postmaster@{1}>'.format(self.FROM_TEXT, domain),
                'to': recipient,
                'subject': 'Nuevo contacto desde pagina web',
                'html': body
            })

        if response.status_code != 200:
            value = '0'
        else:
            value = '1'

        return HttpResponse(value)


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

