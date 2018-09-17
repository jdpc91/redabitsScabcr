#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from rs import session
from rs.consumer import send
from rs.models import Comprobante

API_CLAVE_URL = "http://api.redabits.com/getrespuesta.php?clave=%s"


def receipts():
    """ Return a list of pending receipts

    They are batched in batch of 100 rows
    """
    for receipt in session.query(Comprobante).yield_per(100).filter(
            Comprobante.enviado == False).all():
        yield receipt


def sendall():
    """ Send all pending receipts
    """
    logging.info("Sending pending receipts...")
    for comprobante in receipts():
        resp = send(comprobante)
        if resp.status_code == 200:
            # Revisar respuesta del servidor y actualizar el estado del
            # comprobante
            comprobante.enviado = True
            comprobante.clave = resp.content.strip()
            # FIXME: Coloca la clave en la factura relacionada a Comprobante.
            session.commit()
        else:
            # Problemas con el servidor
            logging.error("Could not get accepted receipt #{}",
                          comprobante.numero_consecutivo)
            logging.info("Will try re-sending receipt #{} on next run",
                         comprobante.numero_consecutivo)