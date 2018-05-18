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

    url(regex='^workinglabs/appointment/$',
        view=views.WorkingLabsAppointmentView.as_view(),
        name='workinglabs_appointment'),

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

    url(regex='^rer/email/homepage$',
        view=views.RERHomepageView.as_view(),
        name='rer_email_homepage'),

    url(regex='^more/contact/$',
        view=views.MoreContactView.as_view(),
        name='more_contact'),

    url(regex='^more/contact/careers1/$',
        view=views.GetMoreCareers1View.as_view(),
        name='getmore_careers1'),

    url(regex='^more/contact/careers2/$',
        view=views.GetMoreCareers2View.as_view(),
        name='getmore_careers2'),

    url(regex='^more/contact/referrals/$',
        view=views.GetMoreReferralsView.as_view(),
        name='getmore_referrals'),

    url(regex='^more/contact/quote/$',
        view=views.GetMoreQuoteView.as_view(),
        name='getmore_quote'),

    url(regex='^more/contact/iidea/$',
        view=views.IideaContacView.as_view(),
        name='iidea_contact'),

    url(regex='^alianza/contact/$',
        view=views.AlianzaContactView.as_view(),
        name='alianza_contact'),

    url(regex='^dimsa/contact/$',
        view=views.DimsaContactView.as_view(),
        name='dimsa_contact'),

    url(regex='^wicore/contact/$',
        view=views.WicoreContactView.as_view(),
        name='wicore_contact'),

    url(regex='^neulift/contact/$',
        view=views.NeuliftContactView.as_view(),
        name='neulift'),

    url(regex='^morelanding/contact/$',
        view=views.MoreLandingContactView.as_view(),
        name='morelanding'),

    url(regex='^entos/contact/$',
        view=views.EntosContactView.as_view(),
        name='entos'),
    
    url(regex='^promor/contact/$',
        view=views.PromorContactView.as_view(),
        name='promor'),

    url(regex='^sic/contact/form/$',
        view=views.SicContactView.as_view(),
        name='sic_contact'),

    url(regex='^sic/quote/form/$',
        view=views.SicQuoteView.as_view(),
        name='quote'),
]