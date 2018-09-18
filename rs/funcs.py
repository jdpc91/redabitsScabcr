#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from rs import session
from rs.consumer import send
from rs.models import Comprobante

CLAVE_URL = "http://api.redabits.com/getrespuesta.php?clave=%s"


def receipts():
    """ Return a list of pending receipts

    They are batched in batch of 100 rows
    """
    for receipt in (
        session.query(Comprobante)
        .yield_per(100)
        .filter(Comprobante.enviado == False)
        .all()
    ):
        yield receipt


def sendall():
    """ Send all pending receipts
    """
    logging.info("Sending pending receipts...")
    for comprobante in receipts():
        resp = send(comprobante)
        clave = resp.content.decode("utf-8").strip()
        if resp.status_code == 200:
            assert clave.isdigit(), "Clave got bogus API response: {}".format(clave)
            comprobante.enviado = True
            comprobante.clave = clave
            factura = comprobante.get_factura()
            factura.folio = clave
            factura.enlace = CLAVE_URL + clave
            session.commit()
        else:
            # Problemas con el servidor
            logging.error(
                "Could not get accepted receipt #{}. API response: {}",
                comprobante.numero_consecutivo,
                clave,
            )
            logging.info(
                "Will try re-sending receipt #{} on next run",
                comprobante.numero_consecutivo,
            )
