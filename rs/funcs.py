#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import tqdm
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
    total = Comprobante.count()
    for comprobante in tqdm.tqdm(receipts(), total=total, ascii=True):
        resp = send(comprobante)
        clave = resp.content.decode("utf-8").strip()
        if clave.isdigit():
            comprobante.enviado = True
            comprobante.clave = clave
            factura = comprobante.get_factura()
            factura.folio = clave
            factura.enlace = CLAVE_URL + clave
            session.commit()
        else:
            # Problemas con el servidor
            logging.error(
                "Could not get accepted receipt #%s. API response: %s",
                comprobante.numero_consecutivo,
                clave,
            )
            logging.info(
                "Will try re-sending receipt #%s on next run",
                comprobante.numero_consecutivo,
            )
