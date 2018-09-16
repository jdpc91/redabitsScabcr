#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rs import session
from rs.consumer import send
from rs.models import Comprobante


def receipts():
    """ Return a list of pending receipts

    They are batched in batch of 100 rows
    """
    yield session.query(Comprobante).yield_per(100).filter(
        Comprobante.enviado == False)


def sendall():
    """ Send all pending receipts
    """
    logging.info("Sending pending receipts...")
    for comprobante in receipts():
        resp = send(comprobante)
        if resp:
            # Revisar respuesta del servidor y actualizar el estado del
            # comprobante
            return resp
        else:
            # Problemas con el servidor
            logging.error("Could not get accepted receipt #{}",
                          comprobante.numero_consecutivo)
            logging.info("Will try re-sending receipt #{} on next run",
                         comprobante.numero_consecutivo)
