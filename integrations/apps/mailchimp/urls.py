#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [

    url(regex='^finacero/newsletter/$',
        view=views.FinaceroNewsletterView.as_view(),
        name='finacero_newsletter'),

    url(regex='^workinglabs/newsletter/$',
        view=views.WorkingLabsNewsletterView.as_view(),
        name='workinglabs_newsletter'),

    url(regex='^rochalandero/newsletter/$',
        view=views.RochaLanderoNewsletterView.as_view(),
        name='rochalandero_newsletter'),

    url(regex='^florelia/newsletter/$',
        view=views.FloreliaNewsletterView.as_view(),
        name='florelia_newsletter'),

]
