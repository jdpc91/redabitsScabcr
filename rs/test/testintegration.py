#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest
from datetime import datetime

from rs.models import Factura


class TestIntegration(unittest.TestCase):
    def setUp(self):
        # Use sandbox/testing capabilities on all other third-party services
        os.environ['DEBUG'] = "ON"

        # Create some invoices, this should trigger the SP and make new
        # receipts
        Factura()._populate()

    def test_send(self):
        """ Send a recipe and see what happens
        """
        from rs.funcs import sendall
        r = sendall()
        assert r
