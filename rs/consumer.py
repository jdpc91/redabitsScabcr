#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from os import getenv
from urllib.parse import urljoin

import requests
from rs.models import Comprobante

AUTH_API_URL = 'http://api.redabits.com/credentials.php'
RECIPE_API_URL = 'http://api.redabits.com/factura.php'
MH_API_BASE = 'https://api.comprobanteselectronicos.go.cr/'
MH_API_PROD = urljoin(MH_API_BASE, 'recepcion/v1')
MH_API_TEST = urljoin(MH_API_BASE, 'recepcion-sandbox/v1')
MH_API_AUTH_TEST = urljoin(
    MH_API_BASE, ('auth/realms/rut-stag/protocol/openid-connect/token'))
MH_API_AUTH_PROD = urljoin(MH_API_BASE,
                           ('auth/realms/rut/protocol/openid-connect/token'))


def auth(comprobante: Comprobante) -> dict:
    """ Ask and set authentication data into the payload
    """
    payload = comprobante.auth_data()
    req = requests.post(AUTH_API_URL, data=payload)
    json = req.json()
    data = comprobante.marshall()
    data['auth'] = json
    data['auth']['documents_endpoint'] = MH_API_TEST if getenv(
        'DEBUG') else MH_API_PROD
    data['auth']['authentication_endpoint'] = MH_API_AUTH_TEST if getenv(
        'DEBUG') else MH_API_AUTH_PROD
    data['auth']['api_client_id'] = 'api-stag' if getenv(
        'DEBUG') else 'api-prod'

    return data


def send(comprobante: Comprobante):
    """ Send the recipe to redabits API server
    """
    payload = auth(comprobante)
    req = requests.post(RECIPE_API_URL, json=payload)
    json = req.json()
    logging.info(json)  # necesito saber que hay de respuesta
