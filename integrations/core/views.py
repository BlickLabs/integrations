#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

import requests
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


class MailgunGenericContactView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(MailgunGenericContactView, self) \
            .dispatch(request, *args, **kwargs)

    def post(self, request):
        key = self.KEY
        domain = self.DOMAIN
        recipient = self.RECIPIENT

        ctx = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'message': request.POST.get('message'),
        }

        body = loader.render_to_string(self.EMAIL_TEMPLATE, ctx)

        endpoint = 'https://api.mailgun.net/v3/{0}/messages'.format(domain)
        response = requests.post(
            endpoint, auth=('api', key), data={
            'from': '{0} <postmaster@{1}>'.format(self.FROM_TEXT, domain),
            'to': recipient,
            'subject': 'Nuevo contacto desde pagina web',
            'text': body
        })

        if response.status_code != 200:
            value = '0'
        else:
            value = '1'

        return HttpResponse(value)


class MailchimpGenericNewsletterView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(MailchimpGenericNewsletterView, self)\
            .dispatch(request, *args, **kwargs)

    def post(self, request):

        key = self.KEY
        list = self.LIST_ID
        shard = self.SHARD

        endpoint = "https://{0}.api.mailchimp.com/3.0/lists/{1}/members/".format(shard, list)

        data = {
            "email_address": request.POST.get('email'),
            "status": "subscribed",
        }

        data = json.dumps(data)

        response = requests.post(
            endpoint,
            auth=('apikey', key),
            data=data
        )
        return JsonResponse(response.json())