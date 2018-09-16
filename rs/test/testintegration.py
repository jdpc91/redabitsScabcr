#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest
from datetime import datetime

from rs import session
from rs.models import Factura


class TestIntegration(unittest.TestCase):
    def setUp(self):
        # Use sandbox/testing capabilities on all other third-party services
        os.environ['DEBUG'] = "ON"

        # Create some invoices, this should trigger the SP and make new
        # receipts. WARNING: There is no rollback between tests, so changes in
        # the tables are accumulative, thus, it may take disk space or add
        # trash to production database if used for testing.
        Factura()._populate()

    def tearDown(self):
        session.rollback()

    def test_send(self):
        """ Send a recipe and see what happens
        """
        from rs.funcs import sendall
        sendall()
