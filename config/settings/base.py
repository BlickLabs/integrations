#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Django settings for integrations
For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

from __future__ import absolute_import, unicode_literals

import environ
import dj_database_url

# DIRS
# -----------------------------------------------------------------------------
ROOT_DIR = environ.Path(__file__) - 3  # (/a/b/myfile.py - 3 = /)
PROJECT_DIR = ROOT_DIR.path('integrations')
APPS_DIR = ROOT_DIR.path('integrations/apps')

env = environ.Env()

# PROJECT APPS
# -----------------------------------------------------------------------------
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    'django.contrib.humanize',

    # Admin
    'django.contrib.admin',
)

THIRD_PARTY_APPS = (
    'suit',
    'corsheaders',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'integrations.apps.mailgun',
    'integrations.apps.mailchimp',
)

INSTALLED_APPS = THIRD_PARTY_APPS + DJANGO_APPS + LOCAL_APPS

# DATABASE
# -----------------------------------------------------------------------------
DATABASES = {
    'default': dj_database_url.config()
}


# MIDDLEWARE CLASSES
# -----------------------------------------------------------------------------
MIDDLEWARE_CLASSES = (
    # Make sure djangosecure.middleware.SecurityMiddleware is listed first
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# MIGRATION
# -----------------------------------------------------------------------------
MIGRATION_MODULES = {
    'sites': 'cookies.contrib.sites.migrations'
}

# FIXTURE CONFIGURATION
# -----------------------------------------------------------------------------
FIXTURE_DIRS = (
    str(PROJECT_DIR.path('fixtures')),
)

# GENERAL CONFIGURATION
# -----------------------------------------------------------------------------
TIME_ZONE = 'America/Mexico_City'

LANGUAGE_CODE = 'en-us'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# TEMPLATE CONFIGURATION
# -----------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(PROJECT_DIR.path('templates')),
        ],
        'OPTIONS': {
            'debug': True,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# URL Configuration
# -----------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

# AUTHENTICATION CONFIGURATION
# -----------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# SUIT CONFIGURATION
# -----------------------------------------------------------------------------
SUIT_CONFIG = {
    'ADMIN_NAME': 'integrations',
}

# STATIC CONFIGURATION
# -----------------------------------------------------------------------------
STATICFILES_DIRS = (
    str(PROJECT_DIR.path('static')),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

CORS_ORIGIN_ALLOW_ALL = True

MAILGUN_API_KEY = env('MAILGUN_API_KEY', default='CHANGEME!!!')

FINACERO_MAILGUN_DOMAIN = env('FINACERO_MAILGUN_DOMAIN', default='CHANGEME!!!')
FINACERO_MAILGUN_RECIPIENT = env('FINACERO_MAILGUN_RECIPIENT', default='CHANGEME!!!')

FINACERO_MAILCHIMP_API_KEY = env('FINACERO_MAILCHIMP_API_KEY', default='CHANGEME!!!')
FINACERO_MAILCHIMP_SHARD = env('FINACERO_MAILCHIMP_SHARD', default='CHANGEME!!!')
FINACERO_MAILCHIMP_LIST_ID = env('FINACERO_MAILCHIMP_LIST_ID', default='CHANGEME!!!')

ROCHA_LANDERO_MAILGUN_DOMAIN = env('ROCHA_LANDERO_MAILGUN_DOMAIN', default='CHANGEME!!!')
ROCHA_LANDERO_MAILGUN_RECIPIENT = env('ROCHA_LANDERO_MAILGUN_RECIPIENT', default='CHANGEME!!!')

ROCHA_LANDERO_MAILCHIMP_API_KEY = env('ROCHA_LANDERO_MAILCHIMP_API_KEY', default='CHANGEME!!!')
ROCHA_LANDERO_MAILCHIMP_SHARD = env('ROCHA_LANDERO_MAILCHIMP_SHARD', default='CHANGEME!!!')
ROCHA_LANDERO_MAILCHIMP_LIST_ID = env('ROCHA_LANDERO_MAILCHIMP_LIST_ID', default='CHANGEME!!!')

WORKING_LABS_MAILGUN_DOMAIN = env('WORKING_LABS_MAILGUN_DOMAIN', default='CHANGEME!!!')
WORKING_LABS_MAILGUN_RECIPIENT = env('WORKING_LABS_MAILGUN_RECIPIENT', default='CHANGEME!!!')

WORKING_LABS_MAILCHIMP_API_KEY = env('WORKING_LABS_MAILCHIMP_API_KEY', default='CHANGEME!!!')
WORKING_LABS_MAILCHIMP_SHARD = env('WORKING_LABS_MAILCHIMP_SHARD', default='CHANGEME!!!')
WORKING_LABS_MAILCHIMP_LIST_ID = env('WORKING_LABS_MAILCHIMP_LIST_ID', default='CHANGEME!!!')

FLORELIA_MAILCHIMP_API_KEY = env('FLORELIA_MAILCHIMP_API_KEY', default='CHANGEME!!!')
FLORELIA_MAILCHIMP_SHARD = env('FLORELIA_MAILCHIMP_SHARD', default='CHANGEME!!!')
FLORELIA_MAILCHIMP_LIST_ID = env('FLORELIA_MAILCHIMP_LIST_ID', default='CHANGEME!!!')

INDOTS_MAILCHIMP_API_KEY = env('INDOTS_MAILCHIMP_API_KEY', default='CHANGEME!!!')
INDOTS_MAILCHIMP_SHARD = env('INDOTS_MAILCHIMP_SHARD', default='CHANGEME!!!')
INDOTS_MAILCHIMP_LIST_ID = env('INDOTS_MAILCHIMP_LIST_ID', default='CHANGEME!!!')

AGUAVIENTO_DOMAIN = env('AGUAVIENTO_DOMAIN', default='CHANGEME!!!')
AGUAVIENTO_RECIPIENT = env('AGUAVIENTO_RECIPIENT', default='CHANGEME!!!')

RGV_DOMAIN = env('RGV_DOMAIN', default='CHANGEME!!!')
RGV_RECIPIENT = env('RGV_RECIPIENT', default='CHANGEME!!!')
RGV_RECIPIENT_CONTACT = env('RGV_RECIPIENT_CONTACT', default='CHANGEME!!!')

RER_MAILGUN_DOMAIN = env('RER_DOMAIN', default='CHANGEME!!!')
RER_MAILGUN_RECIPIENT = env('RER_RECIPIENT', default='CHANGEME!!!')

HIGIA_MAILGUN_DOMAIN = env('HIGIA_DOMAIN', default='CHANGEME!!!')
HIGIA_MAILGUN_RECIPIENT = env('HIGIA_RECIPIENT', default='CHANGEME!!!')
HIGIA_MAILCHIMP_API_KEY = env('HIGIA_MAILCHIMP_API_KEY', default='CHANGEME!!!')
HIGIA_MAILCHIMP_SHARD = env('HIGIA_MAILCHIMP_SHARD', default='CHANGEME!!!')
HIGIA_MAILCHIMP_LIST_ID = env('HIGIA_MAILCHIMP_LIST_ID', default='CHANGEME!!!')

MORE_MAILGUN_DOMAIN = env('MORE_MAILGUN_DOMAIN', default='CHANGEME!!!')
MORE_MAILGUN_RECIPIENT = env('MORE_MAILGUN_RECIPIENT', default='CHANGEME!!!')

IIDEA_MAILGUN_DOMAIN = env('IIDEA_MAILGUN_DOMAIN', default='CHANGEME!!!')
IIDEA_MAILGUN_RECIPIENT = env('IIDEA_MAILGUN_RECIPIENT', default='CHANGEME!!!')

HIGIA_MAILGUN_RECIPIENT = env('HIGIA_MAILGUN_RECIPIENT', default='CHANGEME!!!')

CIERRALO_MAILCHIMP_API_KEY = env('CIERRALO_MAILCHIMP_API_KEY', default='CHANGEME!!!')
CIERRALO_MAILCHIMP_SHARD = env('CIERRALO_MAILCHIMP_SHARD', default='CHANGEME!!!')
CIERRALO_MAILCHIMP_LIST_ID = env('CIERRALO_MAILCHIMP_LIST_ID', default='CHANGEME!!!')

ALIANZA_MAILGUN_DOMAIN = env('ALIANZA_MAILGUN_DOMAIN', default='CHANGEME!!!')
ALIANZA_MAILGUN_RECIPIENT = env('ALIANZA_MAILGUN_RECIPIENT', default='CHANGEME!!!')

ICAN_ES_MAILCHIMP_API_KEY = env('ICAN_ES_MAILCHIMP_API_KEY', default='CHANGEME!!!')
ICAN_ES_MAILCHIMP_SHARD = env('ICAN_ES_MAILCHIMP_SHARD', default='CHANGEME!!!')
ICAN_ES_MAILCHIMP_LIST_ID = env('ICAN_ES_MAILCHIMP_LIST_ID', default='CHANGEME!!!')

ICAN_EN_MAILCHIMP_API_KEY = env('ICAN_EN_MAILCHIMP_API_KEY', default='CHANGEME!!!')
ICAN_EN_MAILCHIMP_SHARD = env('ICAN_EN_MAILCHIMP_SHARD', default='CHANGEME!!!')
ICAN_EN_MAILCHIMP_LIST_ID = env('ICAN_EN_MAILCHIMP_LIST_ID', default='CHANGEME!!!')

DIMSA_MAILGUN_DOMAIN = env('DIMSA_MAILGUN_DOMAIN', default='CHANGEME!!!')
DIMSA_MAILGUN_RECIPIENT = env('DIMSA_MAILGUN_RECIPIENT', default='CHANGEME!!!')

WICORE_MAILGUN_DOMAIN = env('WICORE_MAILGUN_DOMAIN', default='CHANGEME!!!')
WICORE_MAILGUN_RECIPIENT = env('WICORE_MAILGUN_RECIPIENT', default='CHANGEME!!!')

NEULIFT_MAILGUN_DOMAIN = env('NEULIFT_MAILGUN_DOMAIN', default='CHANGEME!!!')
NEULIFT_MAILGUN_RECIPIENT = env('NEULIFT_MAILGUN_RECIPIENT', default='CHANGEME!!!')

MORELANDING_MAILGUN_DOMAIN = env('MORELANDING_MAILGUN_DOMAIN', default='CHANGEME!!!')
MORELANDING_MAILGUN_RECIPIENT = env('MORELANDING_MAILGUN_RECIPIENT', default='CHANGEME!!!')

ENTOS_MAILGUN_DOMAIN = env('ENTOS_MAILGUN_DOMAIN', default='CHANGEME!!!')
ENTOS_MAILGUN_RECIPIENT = env('ENTOS_MAILGUN_RECIPIENT', default='CHANGEME!!!')

PROMOR_MAILGUN_DOMAIN = env('PROMOR_MAILGUN_DOMAIN', default='CHANGEME!!!')
PROMOR_MAILGUN_RECIPIENT = env('PROMOR_MAILGUN_RECIPIENT', default='CHANGEME!!!')

SIC_MAILGUN_DOMAIN = env('SIC_MAILGUN_DOMAIN', default='CHANGEME!!!')
SIC_MAILGUN_RECIPIENT = env('SIC_MAILGUN_RECIPIENT', default='CHANGEME!!!')

SIC_QUOTE_MAILGUN_DOMAIN = env('SIC_QUOTE_MAILGUN_DOMAIN', default='CHANGEME!!!')
SIC_QUOTE_MAILGUN_RECIPIENT = env('SIC_QUOTE_MAILGUN_RECIPIENT', default='CHANGEME!!!')

SIC_CL_MAILGUN_DOMAIN = env('SIC_CL_MAILGUN_DOMAIN', default='CHANGEME!!!')
SIC_CL_MAILGUN_RECIPIENT = env('SIC_CL_MAILGUN_RECIPIENT', default='CHANGEME!!!')

SIC_CL_QUOTE_MAILGUN_DOMAIN = env('SIC_CL_QUOTE_MAILGUN_DOMAIN', default='CHANGEME!!!')
SIC_CL_QUOTE_MAILGUN_RECIPIENT = env('SIC_CL_QUOTE_MAILGUN_RECIPIENT', default='CHANGEME!!!')

SIC_CO_MAILGUN_DOMAIN = env('SIC_CO_MAILGUN_DOMAIN', default='CHANGEME!!!')
SIC_CO_MAILGUN_RECIPIENT = env('SIC_CO_MAILGUN_RECIPIENT', default='CHANGEME!!!')
