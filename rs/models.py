#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import getenv

from rs import session
from sqlalchemy import Boolean, Column, DateTime, Float, Integer, SmallInteger, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import DECIMAL
from sqlalchemy.orm.exc import MultipleResultsFound

BASE = declarative_base()


class Factura(BASE):  # type: ignore
    __tablename__ = "FACTURAS"

    num_factura = Column(Float, primary_key=True, name="NUM_FACTURA")
    cod_pos = Column(String(8), primary_key=True, name="COD_POS")
    tipo = Column(String(11), primary_key=True, name="TIPO")
    fecha = Column(DateTime, nullable=True, name="FECHA")
    monto_total = Column(Float, nullable=True, name="MONTO_TOTAL")
    subtotal = Column(Float, nullable=True, name="SUBTOTAL")
    monto_contado = Column(Float, nullable=True, name="MONTO_CONTADO")
    monto_cheque = Column(Float, nullable=True, name="MONTO_CHEQUE")
    monto_tarjeta = Column(Float, nullable=True, name="MONTO_TARJETA")
    monto_credito = Column(Float, nullable=True, name="MONTO_CREDITO")
    monto_nc = Column(Float, nullable=True, name="MONTO_NC")
    monto_certificado = Column(Float, nullable=True, name="MONTO_CERTIFICADO")
    iv = Column(Float, nullable=True, name="IV")
    vendedor = Column(String(50), nullable=True, name="VENDEDOR")
    cajero = Column(String(50), nullable=True, name="CAJERO")
    cliente = Column(String(50), nullable=True, name="CLIENTE")
    descuento = Column(Float, nullable=True, name="DESCUENTO")
    cod_tarjeta = Column(String(6), nullable=True, name="COD_TARJ")
    observaciones = Column(String(100), nullable=True, name="OBSERVACIONES")
    hilera = Column(String(2000), nullable=True, name="HILERA")
    mensaje_error = Column(String, nullable=True, name="MENSAJE_ERROR")
    cedula = Column(String(20), nullable=True, name="CEDULA")
    cedula_tipo = Column(String(2), nullable=True, name="TIPO_CEDULA")
    correo = Column(String(100), nullable=True, name="CORREO")
    folio = Column(String(250), nullable=True, name="FOLIOMH")
    enlace = Column(String(500), nullable=True, name="LINK")
    enlace_respuesta = Column(String(500), nullable=True, name="LINK_RESPUESTA")
    pdf = Column(String(500), nullable=True, name="LINK_PDF")
    respuesta_hacienda = Column(String(1000), nullable=True, name="RESPUESTA_HACIENDA")
    respuesta_tributacion = Column(
        String(1000), nullable=True, name="RESPUESTA_TRIBUTACION"
    )

    def __repr__(self):
        return "<Factura {} folio {}>".format(self.num_factura, self.folio)

    def get_details(self):
        """ Return a list of purchase details
        """
        linea = 1

        for detail in (
            session.query(Historico)
            .filter(
                Historico.cod_pos == self.cod_pos,
                Historico.num_factura == self.num_factura,
            )
            .all()
        ):
            montototal = detail.cantidad * detail.precio
            montodescuento = montototal * (self.descuento / montototal)
            descuentodesc = "Descuentos otorgados" if montodescuento else ""
            subtotal = montototal - montodescuento
            if detail.iv is None:
                detail.iv = 0
            data = {
                "LineaDetalle": {
                    "NumeroLinea": linea,
                    "Codigo": {"Tipo": "04", "Codigo": detail.codigo.strip()},
                    "Cantidad": detail.cantidad,
                    "UnidadMedida": "Unid",
                    "Detalle": detail.desc_producto,
                    "PrecioUnitario": detail.precio,
                    "MontoTotal": montototal,
                    "MontoDescuento": montodescuento,
                    "NaturalezaDescuento": descuentodesc,
                    "SubTotal": subtotal,
                    "MontoTotalLinea": subtotal + (subtotal * (detail.iv / 100)),
                }
            }
            if detail.iv > 0:
                data["LineaDetalle"]["Impuesto"] = [
                    {
                        "Codigo": "01",
                        "Tarifa": detail.iv,
                        "Monto": subtotal * (detail.iv / 100),
                    }
                ]
            linea = linea + 1
            yield data

    @staticmethod
    def _populate(amount=200):
        """ Add several invoices into the database for testing purpose.
        """
        from mimesis import Generic
        from rs import session
        from datetime import datetime

        g = Generic("es")

        r = session.execute("SELECT TOP 1 [FACTURA_ACTUAL] FROM [dbo].[POS]").first()[0]

        for n in range(int(r), int(r) + amount):
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
                cedula="114760094",  # de Daniel
                correo=g.person.email(),
            )
            session.add(factura)
            session.execute(
                "UPDATE [dbo].[POS] SET [FACTURA_ACTUAL] = [FACTURA_ACTUAL] + 1"
            )
            for detalle in range(5):
                historico = Historico(
                    num_factura=n,
                    cod_pos="TIENDA",
                    tipo="F",
                    codigo="100001",
                    fecha=datetime.now(),
                    cantidad=5,
                    precio=1000,
                    desc_producto=g.food.dish(),
                    proveedor="GENERAL",
                    departamento="IT",
                    costo=0,
                    num_bodega=1,
                    iv=13,
                )
                session.add(historico)
            session.commit()


class Historico(BASE):  # type: ignore
    __tablename__ = "HISTORICO_MOV"

    num_factura = Column(Float, primary_key=True, name="NUM_FACTURA")
    cod_pos = Column(String(8), primary_key=True, name="COD_POS")
    tipo = Column(String(1), primary_key=True, name="TIPO")
    codigo = Column(String(25), primary_key=True, name="CODIGO")
    fecha = Column(DateTime, primary_key=True, name="FECHA")
    cantidad = Column(Float, nullable=True, name="CANTIDAD")
    precio = Column(Float, nullable=True, name="PRECIO")
    desc_producto = Column(String(55), nullable=True, name="DESCRIPCION_PRODUCTO")
    departamento = Column(String(55), nullable=True, name="DEPARTAMENTO")
    proveedor = Column(String(55), nullable=True, name="PROVEEDOR")
    costo = Column(Float, nullable=True, name="COSTO")
    num_bodega = Column(SmallInteger, nullable=True, name="NUM_BODEGA")
    observaciones = Column(String(2000), nullable=True, name="OBSERVACIONES")
    iv = Column(Float, nullable=True, name="IV")

    def __repr__(self):
        return "<Historico {} ({})>".format(self.num_factura, self.cod_pos)


class Comprobante(BASE):  # type: ignore
    __tablename__ = "COMPROBANTE"

    id = Column(Integer, primary_key=True, name="ID")
    clave = Column(String, name="CLAVE")
    num_factura = Column(Float, name="NUM_FACTURA")
    numero_consecutivo = Column(String, name="NUMERO_CONSECUTIVO")
    fecha_emision = Column(DateTime, name="FECHA_EMISION")
    condicion_venta = Column(String(2), name="CONDICION_VENTA")
    medio_pago = Column(String(2), name="MEDIO_PAGO")
    emisor_ident_num = Column(String(50), name="EMISOR_IDENT_NUM")
    emisor_provincia = Column(String(2), name="EMISOR_PROVINCIA")
    emisor_canton = Column(String(3), name="EMISOR_CANTON")
    emisor_distrito = Column(String(3), name="EMISOR_DISTRITO")
    emisor_otras_senas = Column(String(500), name="EMISOR_OTRAS_SENAS")
    receptor_nombre = Column(String(100), nullable=True, name="RECEPTOR_NOMBRE")
    receptor_ident_tipo = Column(String(2), nullable=True, name="RECEPTOR_IDENT_TIPO")
    receptor_ident_num = Column(String(2), nullable=True, name="RECEPTOR_IDENT_NUM")
    resumen_cod_moneda = Column(String(3), name="RESUMEN_COD_MONEDA")
    resumen_tipo_cambio = Column(
        DECIMAL(precision=18, scale=2), nullable=True, name="RESUMEN_TIPO_CAMBIO"
    )
    resumen_total_mercancias_gravadas = Column(
        DECIMAL(precision=18, scale=2), name="RESUMEN_TOTAL_MERCANCIAS_GRAVADAS"
    )
    resumen_total_mercancias_exentas = Column(
        DECIMAL(precision=18, scale=2), name="RESUMEN_TOTAL_MERCANCIAS_EXENTAS"
    )
    resumen_total_gravado = Column(
        DECIMAL(precision=18, scale=2), name="RESUMEN_TOTAL_GRAVADO"
    )
    resumen_total_exento = Column(
        DECIMAL(precision=18, scale=2), name="RESUMEN_TOTAL_EXENTO"
    )
    resumen_total_venta = Column(
        DECIMAL(precision=18, scale=2), name="RESUMEN_TOTAL_VENTA"
    )
    resumen_total_descuentos = Column(
        DECIMAL(precision=18, scale=2), name="RESUMEN_TOTAL_DESCUENTOS"
    )
    resumen_total_venta_neta = Column(
        DECIMAL(precision=18, scale=2), name="RESUMEN_TOTAL_VENTA_NETA"
    )
    resumen_total_impuesto = Column(
        DECIMAL(precision=18, scale=2), name="RESUMEN_TOTAL_IMPUESTO"
    )
    resumen_total_comprobante = Column(
        DECIMAL(precision=18, scale=2), name="RESUMEN_TOTAL_COMPROBANTE"
    )
    normativa_num_resolucion = Column(String(100), name="NORMATIVA_NUM_RESOLUCION")
    normativa_fecha_resolucion = Column(String(100), name="NORMATIVA_FECHA_RESOLUCION")
    otros = Column(String(500), nullable=True, name="OTROS")
    notify_to = Column(String(500), name="NOTIFY_TO")
    notify_from = Column(String(500), name="NOTIFY_FROM")
    papel = Column(String(50), name="PAPEL")
    error = Column(String, nullable=True, name="ERROR")
    enviado = Column(Boolean, name="ENVIADO_API")

    def __repr__(self):
        return "<Comprobante {} clave: {} consecutivo {} estado: {}>".format(
            self.id,
            self.clave,
            self.numero_consecutivo,
            "ENVIADO" if self.enviado else "NO-ENVIADO",
        )

    def auth_data(self) -> dict:
        """ Return a dict with data for authentication
        """
        data = {
            "id": self.emisor_ident_num,
            "entorno": "prueb" if getenv("DEBUG") else "prod",
        }

        return data

    def get_factura(self):
        try:
            return (
                session.query(Factura)
                .filter(Factura.num_factura == self.num_factura)
                .one()
            )
        except MultipleResultsFound:
            raise ValueError("Factura {} esta repetida".format(self.num_factura))

    @staticmethod
    def count():
        """ Return the amount of vouchers to send
        """
        return session.query(Comprobante).filter(Comprobante.enviado == False).count()

    def marshall(self):
        """ Return a dict with all fields
        """
        data = {}
        data["Clave"] = ""
        data["Situacion"] = "1"
        data["NumeroConsecutivo"] = self.numero_consecutivo
        data["FechaEmision"] = self.fecha_emision.isoformat()
        data["CondicionVenta"] = self.condicion_venta
        data["MedioPago"] = self.medio_pago
        data["Emisor"] = {
            "Identificacion": {"Numero": self.emisor_ident_num},
            "Ubicacion": {
                "Provincia": self.emisor_provincia,
                "Canton": self.emisor_canton,
                "Distrito": self.emisor_distrito,
                "OtrasSenas": self.emisor_otras_senas,
            },
            "Telefono": {"CodigoPais": "506"},
        }
        data["Receptor"] = {
            "Nombre": self.receptor_nombre,
            "Identificacion": {
                "Tipo": self.receptor_ident_tipo,
                "Numero": self.receptor_ident_num,
            },
        }
        data["DetalleServicio"] = []
        factura = self.get_factura()
        gravado, exento, descuentos, impuestos = 0.0, 0.0, 0.0, 0.0
        for detail in factura.get_details():
            data["DetalleServicio"].append(detail)
            linea = detail["LineaDetalle"]
            # FIXME: This is a list, be careful
            if "Impuesto" in linea:
                gravado = gravado + linea["SubTotal"]
                impuestos = impuestos + linea["Impuesto"][0]["Monto"]
            else:
                exento = exento + linea["SubTotal"]

            if linea["MontoDescuento"] > 0:
                descuentos = descuentos + linea["MontoDescuento"]
        # This is hacky. Update the record here.
        # Suma de "SubTotal" de las linea que tengan "Impuesto"
        self.resumen_total_mercancias_gravadas = gravado
        # Suma de "SubTotal" de las lineas sin "Impuesto"
        self.resumen_total_mercancias_exentas = exento
        # Igual que `self.resumen_total_mercancias_gravadas`
        self.resumen_total_gravado = gravado
        # Igual que `self.resumen_total_mercancias_exentas`
        self.resumen_total_exento = exento
        # `self.resumen_total_mercancias_gravadas` + `self.resumen_total_mercancias_exentas`
        self.resumen_total_venta = gravado + exento
        # Suma de 'MontoDescuento' de las lineas de detalle
        self.resumen_total_descuentos = descuentos
        # "TotalVenta" - "TotalDescuentos"
        self.resumen_total_venta_neta = (gravado + exento) - descuentos
        # Suma de 'Monto' en 'Impuesto' de todas las lineas de detalle
        self.resumen_total_impuesto = impuestos
        # 'TotalVentaNeta' + 'TotalImpuesto'
        self.resumen_total_comprobante = (gravado + exento + impuestos) - descuentos
        # Update the record
        session.commit()
        data["ResumenFactura"] = {
            "CodigoMoneda": "CRC",
            "TipoCambio": 1,
            "TotalMercanciasGravadas": float(self.resumen_total_mercancias_gravadas),
            "TotalMercanciasExentas": float(self.resumen_total_exento),
            "TotalGravado": float(self.resumen_total_gravado),
            "TotalExento": float(self.resumen_total_exento),
            "TotalVenta": float(self.resumen_total_venta),
            "TotalDescuentos": float(self.resumen_total_descuentos),
            "TotalVentaNeta": float(self.resumen_total_venta_neta),
            "TotalImpuesto": float(self.resumen_total_impuesto),
            "TotalComprobante": float(self.resumen_total_comprobante),
        }
        data["Normativa"] = {
            "NumeroResolucion": self.normativa_num_resolucion,
            "FechaResolucion": self.normativa_fecha_resolucion,
        }
        data["Otros"] = self.otros
        data["notify"] = {"to": self.notify_to, "from": self.notify_from}
        data["papel"] = self.papel
        assert len(data["DetalleServicio"]) > 0, "`DetallesServicios` can't be empty"

        return data
