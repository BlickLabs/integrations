#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [

    url(regex='^finacero/email/$',
        view=views.FinaceroContactView.as_view(),
        name='finacero_email'),

    url(regex='^rochalandero/email/$',
        view=views.RochaLanderoContactView.as_view(),
        name='rochalandero_email'),

    url(regex='^rochalandero/carrers/$',
        view=views.RochaLanderoCarrerView.as_view(),
        name='rochalandero_email'),

    url(regex='^workinglabs/email/$',
        view=views.WorkingLabsContactView.as_view(),
        name='workinglabs_email'),

    url(regex='^workinglabs/partner/$',
        view=views.WorkingLabsPartnershipView.as_view(),
        name='workinglabs_partner'),

    url(regex='^workinglabs/free/$',
        view=views.WorkingLabsFreeDayView.as_view(),
        name='workinglabs_free'),

    url(regex='^neopraxis/email/$',
        view=views.NeopraxisContact.as_view(),
        name='workinglabs_free'),

]
