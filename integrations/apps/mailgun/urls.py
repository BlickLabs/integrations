#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [

    url(regex='^finacero/email/$',
        view=views.FinaceroContactView.as_view(),
        name='finacero_email'),

    url(regex='^higia/email/$',
        view=views.HigiaContactView.as_view(),
        name='higia_email'),

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

    url(regex='^aguaviento/email/$',
        view=views.AguavientoContact.as_view(),
        name='aguaviento_contact'),

    url(regex='^rgv/email/$',
        view=views.RGVContact.as_view(),
        name='rgv_contact'),

    url(regex='^rgv/opportunities/$',
        view=views.RGVOpportunitiesView.as_view(),
        name='rgv_contact_opportunities'),

    url(regex='^rer/email/$',
        view=views.RERContactView.as_view(),
        name='rer_email'),

    url(regex='^rer/contact/$',
        view=views.RERContactWithCompanyView.as_view(),
        name='rer_contact'),

    url(regex='^getmore/contact/$',
        view=views.MoreContactView.as_view(),
        name='more_contact')
]
