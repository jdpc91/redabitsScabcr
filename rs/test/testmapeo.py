#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Prueba si el mapeo de modelos a tablas funciona en MSSQL.
"""

import unittest

from rs import session
from rs.models import Factura, Historico


class TestMapeo(unittest.TestCase):
    def test_factura(self):
        """ Consigue cualquier cosa de la tabla FACTURAS
        """
        obj = session.query(Factura).filter(Factura.num_factura == 35.0).all()

    def test_historico(self):
        """ Consigue cualquier cosa de la tabla HISTORICO_MOV
        """
        obj = session.query(Historico).filter(
            Historico.num_factura == 602.0).all()
