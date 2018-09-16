#!/usr/bin/env python
# -*- coding: utf-8 -*-

import http.client as http_client
import json
import logging
from os import getenv
from urllib.parse import urljoin

import requests
from rs.models import Comprobante

AUTH_API_URL = 'http://api.redabits.com/credentials.php'
RECIPE_API_URL = 'http://api.redabits.com:3000/factura'
MH_API_BASE = 'https://api.comprobanteselectronicos.go.cr/'
MH_API_PROD = urljoin(MH_API_BASE, 'recepcion/v1')
MH_API_TEST = urljoin(MH_API_BASE, 'recepcion-sandbox/v1')
MH_API_AUTH_TEST = urljoin(
    MH_API_BASE, ('auth/realms/rut-stag/protocol/openid-connect/token'))
MH_API_AUTH_PROD = urljoin(MH_API_BASE,
                           ('auth/realms/rut/protocol/openid-connect/token'))

if getenv('DEBUG'):
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


def auth(comprobante: Comprobante) -> dict:
    """ Ask and set authentication data into the payload
    """
    payload = comprobante.auth_data()
    req = requests.post(AUTH_API_URL, data=payload)
    logging.debug(req.content)
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
    logging.debug(json.dumps(payload))
    req = requests.post(RECIPE_API_URL, json=payload)
    logging.debug(req.content)
    return req
