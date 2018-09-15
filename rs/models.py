#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, Float, DateTime, SmallInteger
from sqlalchemy.types import DECIMAL
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()


class Factura(BASE):
    __tablename__ = 'FACTURAS'

    num_factura = Column(Float, primary_key=True, name='NUM_FACTURA')
    cod_pos = Column(String(8), primary_key=True, name='COD_POS')
    tipo = Column(String(11), primary_key=True, name='TIPO')
    fecha = Column(DateTime, nullable=True, name='FECHA')
    monto_total = Column(Float, nullable=True, name='MONTO_TOTAL')
    subtotal = Column(Float, nullable=True, name='SUBTOTAL')
    monto_contado = Column(Float, nullable=True, name='MONTO_CONTADO')
    monto_cheque = Column(Float, nullable=True, name='MONTO_CHEQUE')
    monto_tarjeta = Column(Float, nullable=True, name='MONTO_TARJETA')
    monto_credito = Column(Float, nullable=True, name='MONTO_CREDITO')
    monto_nc = Column(Float, nullable=True, name='MONTO_NC')
    monto_certificado = Column(Float, nullable=True, name='MONTO_CERTIFICADO')
    iv = Column(Float, nullable=True, name='IV')
    vendedor = Column(String(50), nullable=True, name='VENDEDOR')
    cajero = Column(String(50), nullable=True, name='CAJERO')
    cliente = Column(String(50), nullable=True, name='CLIENTE')
    descuento = Column(Float, nullable=True, name='DESCUENTO')
    cod_tarjeta = Column(String(6), nullable=True, name='COD_TARJ')
    observaciones = Column(String(250), nullable=True, name='OBSERVACIONES')
    mensaje_error = Column(String, nullable=True, name='MENSAJE_ERROR')
    cedula = Column(String(20), nullable=True, name='CEDULA')
    correo = Column(String(100), nullable=True, name='CORREO')
    folio = Column(String(250), nullable=True, name='FOLIOMH')
    enlace = Column(String(500), nullable=True, name='LINK')
    enlace_respuesta = Column(
        String(500), nullable=True, name='LINK_RESPUESTA')
    pdf = Column(String(500), nullable=True, name='LINK_PDF')
    respuesta_hacienda = Column(
        String(1000), nullable=True, name='RESPUESTA_HACIENDA')
    respuesta_tributacion = Column(
        String(1000), nullable=True, name='RESPUESTA_TRIBUTACION')


class Historico(BASE):
    __tablename__ = "HISTORICO_MOV"

    num_factura = Column(Float, primary_key=True, name='NUM_FACTURA')
    cod_pos = Column(String(8), primary_key=True, name='COD_POS')
    tipo = Column(String(1), primary_key=True, name='TIPO')
    codigo = Column(String(25), primary_key=True, name='CODIGO')
    fecha = Column(DateTime, primary_key=True, name='FECHA')
    cantidad = Column(Float, nullable=True, name='CANTIDAD')
    precio = Column(Float, nullable=True, name='PRECIO')
    desc_producto = Column(
        String(55), nullable=True, name='DESCRIPCION_PRODUCTO')
    departamento = Column(String(55), nullable=True, name='DEPARTAMENTO')
    proveedor = Column(String(55), nullable=True, name='PROVEEDOR')
    costo = Column(Float, nullable=True, name='COSTO')
    num_bodega = Column(SmallInteger, nullable=True, name='NUM_BODEGA')
    observaciones = Column(String(2000), nullable=True, name='OBSERVACIONES')
    iv = Column(Float, nullable=True, name='IV')


class Comprobante(BASE):
    __tablename__ = "COMPROBANTE"

    id = Column(Integer, primary_key=True, name='ID')
    clave = Column(String, name='CLAVE')
    numero_consecutivo = Column(String, name='NUMERO_CONSECUTIVO')
    fecha_emision = Column(DateTime, name='FECHA_EMISION')
    condicion_venta = Column(String(2), name='CONDICION_VENTA')
    medio_pago = Column(String(2), name='MEDIO_PAGO')
    emisor_nombre = Column(String(100), name='EMISOR_NOMBRE')
    emisor_ident_tipo = Column(String(2), name="EMISOR_IDENT_TIPO")
    emisor_ident_num = Column(String(50), name="EMISOR_IDENT_NUM")
    emisor_nombre_comercial = Column(
        String(500), name='EMISOR_NOMBRE_COMERCIAL')
    emisor_provincia = Column(String(2), name='EMISOR_PROVINCIA')
    emisor_canton = Column(String(3), name='EMISOR_CANTON')
    emisor_distrito = Column(String(3), name='EMISOR_DISTRITO')
    emisor_otras_senas = Column(String(500), name='EMISOR_OTRAS_SENAS')
    emisor_tel_cod_pais = Column(Integer, name='EMISOR_TEL_COD_PAIS')
    emisor_tel_num = Column(String(50), name='EMISOR_TEL_NUM')
    emisor_correo_elec = Column(String(100), name='EMISOR_CORREO_ELEC')
    receptor_nombre = Column(
        String(100), nullable=True, name='RECEPTOR_NOMBRE')
    receptor_ident_tipo = Column(
        String(2), nullable=True, name='RECEPTOR_IDENT_TIPO')
    receptor_ident_num = Column(
        String(2), nullable=True, name='RECEPTOR_IDENT_NUM')
    resumen_cod_moneda = Column(String(3), name='RESUMEN_COD_MONEDA')
    resumen_tipo_cambio = Column(
        DECIMAL(precision=18, scale=2),
        nullable=True,
        name='RESUMEN_TIPO_CAMBIO')
    resumen_total_mercancias_gravadas = Column(
        DECIMAL(precision=18, scale=2),
        name='RESUMEN_TOTAL_MERCANCIAS_GRAVADAS')
    resumen_total_mercancias_exentas = Column(
        DECIMAL(precision=18, scale=2),
        name='RESUMEN_TOTAL_MERCANCIAS_EXENTAS')
    resumen_total_gravado = Column(
        DECIMAL(precision=18, scale=2), name='RESUMEN_TOTAL_GRAVADO')
    resumen_total_exento = Column(
        DECIMAL(precision=18, scale=2), name='RESUMEN_TOTAL_EXENTO')
    resumen_total_venta = Column(
        DECIMAL(precision=18, scale=2), name='RESUMEN_TOTAL_VENTA')
    resumen_total_descuentos = Column(
        DECIMAL(precision=18, scale=2), name='RESUMEN_TOTAL_DESCUENTOS')
    resumen_total_venta_neta = Column(
        DECIMAL(precision=18, scale=2), name='RESUMEN_TOTAL_VENTA_NETA')
    resumen_total_impuesto = Column(
        DECIMAL(precision=18, scale=2), name='RESUMEN_TOTAL_IMPUESTO')
    resumen_total_comprobante = Column(
        DECIMAL(precision=18, scale=2), name='RESUMEN_TOTAL_COMPROBANTE')
    normativa_num_resolucion = Column(
        String(100), name='NORMATIVA_NUM_RESOLUCION')
    normativa_fecha_resolucion = Column(
        String(100), name='NORMATIVA_FECHA_RESOLUCION')
    otros = Column(String(500), nullable=True, name='OTROS')
    auth_usuario = Column(String(500), name='AUTH_USUARIO')
    auth_password = Column(String, name='AUTH_PASSWORD')
    auth_cert = Column(String, name='AUTH_CERT')
    auth_pin = Column(String(500), name='AUTH_PIN')
    auth_documents_endpoint = Column(
        String(500), name='AUTH_DOCUMENTS_ENDPOINT')
    auth_api_client_id = Column(String(50), name='AUTH_API_CLIENT_ID')
    notify_to = Column(String(500), name='NOTIFY_TO')
    notify_from = Column(String(500), name='NOTIFY_FROM')
    papel = Column(String(50), name='PAPEL')


class ComprobanteDetalle(BASE):
    __tablename__ = 'COMPROBANTE_LINEA_DETALLE'

    id = Column(Integer, primary_key=True, name="ID")
    comprobante_id = Column(Integer, name='COMPROBANTE_ID')
    numero_linea = Column(Integer, name='NUMERO_LINEA')
    codigo_tipo = Column(String(2), name='CODIGO_TIPO')
    codigo_cod = Column(String(50), name='CODIGO_COD')
    cantidad = Column(Integer, name='CANTIDAD')
    unidad_medida = Column(String(50), name='UNIDAD_MEDIDA')
    detalle = Column(String(500), name='DETALLE')
    precio_unitario = Column(
        DECIMAL(precision=18, scale=2), name='PRECIO_UNITARIO')
    monto_total = Column(DECIMAL(precision=18, scale=2), name='MONTO_TOTAL')
    monto_descuento = Column(
        DECIMAL(precision=18, scale=2), nullable=True, name='MONTO_DESCUENTO')
    naturaleza_descuento = Column(
        String(100), nullable=True, name='NATURALEZA_DESCUENTO')
    subtotal = Column(DECIMAL(precision=18, scale=2), name='SUBTOTAL')
    impuesto_codigo = Column(String(2), nullable=True, name='IMPUESTO_CODIGO')
    impuesto_tarifa = Column(String(2), nullable=True, name='IMPUESTO_TARIFA')
    impuesto_monto = Column(
        DECIMAL(precision=18, scale=2), nullable=True, name='IMPUESTO_MONTO')
    monto_total_linea = Column(
        DECIMAL(precision=18, scale=2), name='MONTO_TOTAL_LINEA')
