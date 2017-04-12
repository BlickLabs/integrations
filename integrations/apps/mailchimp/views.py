#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf import settings

from integrations.core.views import MailchimpGenericNewsletterView


class FinaceroNewsletterView(MailchimpGenericNewsletterView):
    KEY = settings.FINACERO_MAILCHIMP_API_KEY
    LIST_ID = settings.FINACERO_MAILCHIMP_LIST_ID
    SHARD = settings.FINACERO_MAILCHIMP_SHARD


class WorkingLabsNewsletterView(MailchimpGenericNewsletterView):
    KEY = settings.WORKING_LABS_MAILCHIMP_API_KEY
    LIST_ID = settings.WORKING_LABS_MAILCHIMP_LIST_ID
    SHARD = settings.WORKING_LABS_MAILCHIMP_SHARD


class RochaLanderosNewsletterView(MailchimpGenericNewsletterView):
    KEY = settings.ROCHA_LANDEROS_MAILCHIMP_API_KEY
    LIST_ID = settings.ROCHA_LANDEROS_MAILCHIMP_LIST_ID
    SHARD = settings.ROCHA_LANDEROS_MAILCHIMP_SHARD


class FloreliaNewsletterView(MailchimpGenericNewsletterView):
    KEY = settings.FLORELIA_MAILCHIMP_API_KEY
    LIST_ID = settings.FLORELIA_MAILCHIMP_LIST_ID
    SHARD = settings.FLORELIA_MAILCHIMP_SHARD
