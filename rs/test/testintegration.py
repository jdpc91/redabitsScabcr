#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest
from datetime import datetime
from rs.consumer import send


class TestIntegration(unittest.TestCase):
    def setUp(self):
        # Use sandbox/testing capabilities on all other third-party services
        os.environ['DEBUG'] = "ON"

        # Import here after setting DEBUG as ON
        from rs import session
        from rs.models import Comprobante, ComprobanteDetalle

        # Add a new recipe
        cd1 = ComprobanteDetalle(
            numero_linea=100,
            codigo_tipo='01',
            codigo_cod='1234567890',
            cantidad=1,
            unidad_medida='unidad',
            detalle='detalle',
            precio_unitario=10.0,
            monto_total=10.0,
            monto_descuento=0,
            naturaleza_descuento="ninguno",
            subtotal=10.0,
            impuesto_codigo="01",
            impuesto_tarifa="01",
            impuesto_monto=0,
            monto_total_linea=0)
        self.cp = Comprobante(
            clave="50613091811560029470300100001010000001336173667076",
            numero_consecutivo="00100001010000001336",
            fecha_emision=datetime.now(),
            condicion_venta="00",
            medio_pago="00",
            emisor_nombre="Nombre",
            emisor_ident_tipo="03",
            emisor_ident_num="115600294703",
            emisor_nombre_comercial="SUPER PRUEBA 2000",
            emisor_provincia="00",
            emisor_canton="00",
            emisor_distrito="00",
            emisor_otras_senas="Costa Rica",
            emisor_tel_cod_pais="506",
            emisor_tel_num="0000000",
            emisor_correo_elec="correo@prueba.org",
            receptor_nombre="Nombre",
            receptor_ident_tipo="03",
            receptor_ident_num="115600294703",
            resumen_cod_moneda="CRC",
            resumen_tipo_cambio="150/123",
            resumen_total_mercancias_gravadas=0,
            resumen_total_mercancias_exentas=0,
            resumen_total_gravado=0,
            resumen_total_exento=0,
            resumen_total_venta=0,
            resumen_total_descuentos=0,
            resumen_total_venta_neta=0,
            resumen_total_impuesto=0,
            resumen_total_comprobante=0,
            normativa_num_resolucion="DGT-R-48-2016",
            normativa_fecha_resolucion=datetime.now(),
            otros="Otros",
            notify_to="hola@mundo.com",
            notify_from="adios@mundo.com",
            papel="tiquete")
        self.cp.comprobante_detalle = [cd1, cd1, cd1]
        # añade los nuevos objetos a la base de datos
        session.add(self.cp)
        session.commit()

    def test_send(self):
        """ Send a recipe and see what happens
        """
        send(self.cp)
