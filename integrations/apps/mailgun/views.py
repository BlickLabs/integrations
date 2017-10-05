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

class HigiaContactView(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.HIGIA_MAILGUN_DOMAIN
    RECIPIENT = settings.HIGIA_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/generic_contact.html'
    FROM_TEXT = 'Higia'
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
    EMAIL_TEMPLATE = 'email/rocha_landero_carrers.html'
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


class AguavientoContact(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.AGUAVIENTO_DOMAIN
    RECIPIENT = settings.AGUAVIENTO_RECIPIENT
    EMAIL_TEMPLATE = 'email/generic_contact.html'
    FROM_TEXT = 'Aguaviento'
    SUBJECT = 'Nuevo contacto desde página web:Aguaviento'


class RGVContact(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.RGV_DOMAIN
    RECIPIENT = settings.RGV_RECIPIENT_CONTACT
    EMAIL_TEMPLATE = 'email/generic_contact.html'
    FROM_TEXT = 'RGV'
    SUBJECT = 'Nuevo contacto desde página web:RGV'


class RGVOpportunitiesView(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.RGV_DOMAIN
    RECIPIENT = settings.RGV_RECIPIENT
    EMAIL_TEMPLATE = 'email/RGV_opportunities.html'
    FROM_TEXT = 'RGV'
    SUBJECT = 'Nuevo contacto desde Oportunidades'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(RGVOpportunitiesView, self) \
            .dispatch(request, *args, **kwargs)

    def post(self, request):
        ctx = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
            'birthday': request.POST.get('birthday'),
            'title': request.POST.get('title')
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


class RERContactView(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.RER_MAILGUN_DOMAIN
    RECIPIENT = settings.RER_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/generic_contact.html'
    FROM_TEXT = 'RER Energy Group'
    SUBJECT = 'Nuevo contacto desde pagina web'


class GetMoreCareers1View(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.MORE_MAILGUN_DOMAIN
    RECIPIENT = settings.MORE_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/More_careers1.html'
    FROM_TEXT = 'More'
    SUBJECT = 'Nuevo contacto desde página web:Careers'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(GetMoreCareers1View, self) \
            .dispatch(request, *args, **kwargs)

    def post(self, request):
        ctx = {
            'nameCareers': request.POST.get('nameCareers'),
            'emailCareers': request.POST.get('emailCareers'),
            'phoneCareers': request.POST.get('phoneCareers'),
            'openingCareers': request.POST.get('openingCareers'),
            'linkedinCareers': request.POST.get('linkedinCareers')
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