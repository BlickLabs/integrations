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

class WorkingLabsAppointmentView(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.WORKING_LABS_MAILGUN_DOMAIN
    RECIPIENT = settings.WORKING_LABS_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/working_labs_appointment.html'
    FROM_TEXT = 'Working Labs'
    SUBJECT = 'Nuevo agendación para cita'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(WorkingLabsAppointmentView, self) \
            .dispatch(request, *args, **kwargs)

    def post(self, request):
        ctx = {
            'completename': request.POST.get('completename'),
            'telnumber': request.POST.get('telnumber'),
            'peopleteam': request.POST.get('peopleteam'),
            'date': request.POST.get('date'),
            'time': request.POST.get('time'),
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
    EMAIL_TEMPLATE = 'email/RER_contact.html'
    FROM_TEXT = 'RER Energy Group'
    SUBJECT = 'Nuevo contacto desde pagina web'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(RERContactView, self) \
            .dispatch(request, *args, **kwargs)

    def post(self, request):
        ctx = {
            'contactname': request.POST.get('contactname'),
            'contactlastname': request.POST.get('contactlastname'),
            'contactemail': request.POST.get('contactemail'),
            'contactcompany': request.POST.get('contactcompany'),
            'contactmessage': request.POST.get('contactmessage')
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

class RERHomepageView(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.RER_MAILGUN_DOMAIN
    RECIPIENT = settings.RER_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/RER_homepage.html'
    FROM_TEXT = 'RER Energy Group'
    SUBJECT = 'Nuevo contacto desde pagina web'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(RERHomepageView, self) \
            .dispatch(request, *args, **kwargs)

    def post(self, request):
        ctx = {
            'candidatename': request.POST.get('candidatename'),
            'candidateemail': request.POST.get('candidateemail'),
            'candidatemessage': request.POST.get('candidatemessage')
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


class MoreContactView(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.MORE_MAILGUN_DOMAIN
    RECIPIENT = settings.MORE_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/generic_contact.html'
    FROM_TEXT = 'More'
    SUBJECT = 'Nuevo contacto desde página web:More'


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


class GetMoreCareers2View(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.MORE_MAILGUN_DOMAIN
    RECIPIENT = settings.MORE_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/More_careers2.html'
    FROM_TEXT = 'More'
    SUBJECT = 'Nuevo contacto desde página web:Careers'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(GetMoreCareers2View, self) \
            .dispatch(request, *args, **kwargs)

    def post(self, request):
        ctx = {
            'LiCareers': request.POST.get('LiCareers'),
            'portfolioCareers': request.POST.get('portfolioCareers'),
            'githubCareers': request.POST.get('githubCareers'),
            'urlCareers': request.POST.get('urlCareers'),
            'whyMoreCareers': request.POST.get('whyMoreCareers')
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


class GetMoreReferralsView(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.MORE_MAILGUN_DOMAIN
    RECIPIENT = settings.MORE_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/More_referrals.html'
    FROM_TEXT = 'More'
    SUBJECT = 'Nuevo contacto desde página web:Referrals'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(GetMoreReferralsView, self) \
            .dispatch(request, *args, **kwargs)

    def post(self, request):
        ctx = {
            'nameReferrals': request.POST.get('nameReferrals'),
            'mailReferrals': request.POST.get('mailReferrals'),
            'phoneReferrals': request.POST.get('phoneReferrals'),
            'messageReferrals': request.POST.get('messageReferrals')
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


class GetMoreQuoteView(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.MORE_MAILGUN_DOMAIN
    RECIPIENT = settings.MORE_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/More_quote.html'
    FROM_TEXT = 'More'
    SUBJECT = 'Nuevo contacto desde página web:Quote'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(GetMoreQuoteView, self) \
            .dispatch(request, *args, **kwargs)

    def post(self, request):
        ctx = {
            'nameQuote': request.POST.get('nameQuote'),
            'phoneQuote': request.POST.get('phoneQuote'),
            'projectTypeQuote': request.POST.get('projectTypeQuote'),
            'emailQuote': request.POST.get('emailQuote'),
            'projectNameQuote': request.POST.get('projectNameQuote'),
            'budgetQuote': request.POST.get('budgetQuote'),
            'detailsQuote': request.POST.get('detailsQuote')
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


class IideaContacView(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.IIDEA_MAILGUN_DOMAIN
    RECIPIENT = settings.IIDEA_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/generic_contact.html'
    FROM_TEXT = 'Iidea'
    SUBJECT = 'Nuevo contacto desde página web:Iidea'


class AlianzaContactView(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.ALIANZA_MAILGUN_DOMAIN
    RECIPIENT = settings.ALIANZA_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/generic_contact.html'
    FROM_TEXT = 'Alianza SweMex'
    SUBJECT = 'Nuevo contacto desde página web'


class DimsaContactView(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.DIMSA_MAILGUN_DOMAIN
    RECIPIENT = settings.DIMSA_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/generic_contact.html'
    FROM_TEXT = 'DIM - SA'
    SUBJECT = 'Nuevo contacto desde página web'


class WicoreContactView(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.WICORE_MAILGUN_DOMAIN
    RECIPIENT = settings.WICORE_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/generic_contact.html'
    FROM_TEXT = 'wiCore'
    SUBJECT = 'Nuevo contacto desde página web'


class NeuliftContactView(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.NEULIFT_MAILGUN_DOMAIN
    RECIPIENT = settings.NEULIFT_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/generic_contact.html'
    FROM_TEXT = 'Neulift'
    SUBJECT = 'Nuevo contacto desde www.neulift.com.mx'


class MoreLandingContactView(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.MORELANDING_MAILGUN_DOMAIN
    RECIPIENT = settings.MORELANDING_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/generic_contact.html'
    FROM_TEXT = 'More Co. | Shopify Experts'
    SUBJECT = 'Nuevo mensaje desde www.shop.getmore.mx'


class EntosContactView(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.ENTOS_MAILGUN_DOMAIN
    RECIPIENT = settings.ENTOS_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/generic_contact.html'
    FROM_TEXT = 'Entos | Innovation Beyond Measure'
    SUBJECT = 'New message from landing page.'


class PromorContactView(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.PROMOR_MAILGUN_DOMAIN
    RECIPIENT = settings.PROMOR_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/generic_contact.html'
    FROM_TEXT = 'Promor'
    SUBJECT = 'Nuevo contacto desde pagina web'

class SicContactView(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.SIC_MAILGUN_DOMAIN
    RECIPIENT = settings.SIC_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/generic_contact.html'
    FROM_TEXT = 'SIC | Comercialización y Servicios'
    SUBJECT = 'Nuevo mensaje desde www.sic.com.mx.'

class SicQuoteView(MailgunGenericContactView):
    KEY = settings.MAILGUN_API_KEY
    DOMAIN = settings.SIC_QUOTE_MAILGUN_DOMAIN
    RECIPIENT = settings.SIC_QUOTE_MAILGUN_RECIPIENT
    EMAIL_TEMPLATE = 'email/generic_contact.html'
    FROM_TEXT = 'SIC | Comercialización y Servicios'
    SUBJECT = 'Nuevo mensaje desde www.sic.com.mx.'
