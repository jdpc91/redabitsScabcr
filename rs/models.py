#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import getenv

from rs import session
from sqlalchemy import (Boolean, Column, DateTime, Float, ForeignKey, Integer,
                        SmallInteger, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.types import DECIMAL

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

    @staticmethod
    def _populate(amount=200):
        """ Add several invoices into the database for testing purpose.
        """
        from mimesis import Generic
        from rs import session

        g = Generic('es')

        for n in range(amount):
            folio = g.code.pin("5060209180001081103###########"
                               "######00008161887157")
            factura = Factura(
                num_factura=n,
                cod_pos="TIENDA",
                tipo="F",
                monto_total=n,
                subtotal=n,
                monto_contado=n,
                monto_cheque=0,
                monto_tarjeta=0,
                monto_credito=0,
                monto_nc=0,
                monto_certificado=0,
                iv=0,
                vendedor=g.person.full_name(),
                cajero=g.person.full_name(),
                cliente=g.person.full_name(),
                descuento=0,
                cedula='114760094',  # de Daniel
                correo=g.person.email(),
                folio=folio,
                enlace="http://api.redabits.com/getrespuesta.php?clave=" +
                folio)
            session.add(factura)

            try:
                session.commit()
            except:
                session.rollback()


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
    comprobante_detalle = relationship('ComprobanteDetalle')
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
    notify_to = Column(String(500), name='NOTIFY_TO')
    notify_from = Column(String(500), name='NOTIFY_FROM')
    papel = Column(String(50), name='PAPEL')
    error = Column(String, nullable=True, name='ERROR')
    enviado = Column(Boolean, name='ENVIADO_API')

    def auth_data(self) -> dict:
        """ Return a dict with data for authentication
        """
        data = {
            'id': self.emisor_ident_num,
            'entorno': 'prueb' if getenv('DEBUG') else 'prod',
        }

        return data

    @classmethod
    def get_details(cls, id):
        """ Return a list of `ComprobanteDetalle`
        """
        return session.query(ComprobanteDetalle).filter(
            ComprobanteDetalle.comprobante_id == id).all()

    def marshall(self):
        """ Return a dict with all fields
        """
        data = {}
        data['NumeroConsecutivo'] = self.numero_consecutivo
        data['FechaEmision'] = self.fecha_emision.isoformat()
        data['CondicionVenta'] = self.condicion_venta
        data['MedioPago'] = self.medio_pago
        data['Emisor'] = {
            'Nombre': self.emisor_nombre,
            'Identificacion': {
                'Tipo': self.emisor_ident_tipo,
                'Numero': self.emisor_ident_num,
            },
            'NombreComercial': self.emisor_nombre_comercial,
            'Ubicacion': {
                'Provincia': self.emisor_provincia,
                'Canton': self.emisor_canton,
                'Distrito': self.emisor_distrito,
                'OtrasSenas': self.emisor_otras_senas,
            },
            "Telefono": {
                'CodigoPais': self.emisor_tel_cod_pais,
                'NumTelefono': self.emisor_tel_num,
            },
            "CorreoElectronico": self.emisor_correo_elec
        }
        data['Receptor'] = {
            'Nombre': self.receptor_nombre,
            'Identificacion': {
                'Tipo': self.receptor_ident_tipo,
                'Numero': self.receptor_ident_num,
            }
        }
        data['DetallesServicio'] = []
        for detalle in Comprobante.get_details(self.id):
            d = {
                'LineaDetalle': {
                    'NumeroLinea': detalle.numero_linea,
                    'Codigo': {
                        'Tipo': detalle.codigo_tipo,
                        'Codigo': detalle.codigo_cod
                    },
                    'Cantidad': detalle.cantidad,
                    'UnidadMedida': detalle.unidad_medida,
                    'Detalle': detalle.detalle,
                    'PrecioUnitario': detalle.precio_unitario,
                    "MontoTotal": detalle.monto_total,
                    "MontoDescuento": detalle.monto_descuento,
                    "NaturalezaDescuento": detalle.naturaleza_descuento,
                    "SubTotal": detalle.subtotal,
                    "Impuesto": {
                        "Codigo": detalle.impuesto_codigo,
                        "Tarifa": detalle.impuesto_tarifa,
                        "Monto": detalle.impuesto_monto,
                    },
                    "MontoTotalLinea": detalle.monto_total_linea,
                }
            }
            data['DetalleServicio'].append(d)
        data['ResumenFactura'] = {
            'CodigoMoneda': self.resumen_cod_moneda,
            'TipoCambio': self.resumen_tipo_cambio,
            'TotalMercanciasGravadas': self.resumen_total_mercancias_gravadas,
            'TotalMercanciasExentas': self.resumen_total_exento,
            'TotalGravado': self.resumen_total_gravado,
            'TotalExento': self.resumen_total_exento,
            'TotalVenta': self.resumen_total_venta,
            'TotalDescuentos': self.resumen_total_descuentos,
            'TotalVentaNeta': self.resumen_total_venta_neta,
            'TotalImpuesto': self.resumen_total_impuesto,
            'TotalComprobante': self.resumen_total_comprobante,
        }
        data['Normativa'] = {
            'NumeroResolucion': self.normativa_num_resolucion,
            'FechaResolucion': self.normativa_fecha_resolucion.isoformat(),
        }
        data['Otros'] = self.otros
        # NOTA: El bloque de AUTH fue ignorado porque esa informacion se
        # adquiere de otro recurso y no desde la base de datos
        data['notify'] = {
            "to": self.notify_to,
            "from": self.notify_from,
        }
        data['papel'] = self.papel

        return data


class ComprobanteDetalle(BASE):
    __tablename__ = 'COMPROBANTE_LINEA_DETALLE'

    id = Column(Integer, primary_key=True, name="ID")
    comprobante_id = Column('COMPROBANTE_ID', Integer,
                            ForeignKey('COMPROBANTE.ID'))
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
