[ID] [int] IDENTITY(1,1) NOT NULL, -- Autogenerado
[CLAVE] [varchar](max) NOT NULL, --  FACTURAS.[FOLIOMH]
[NUMERO_CONSECUTIVO] [varchar](max) NOT NULL, --se podria calcular con trigger
-- 001-00001-01-0000000001
-- oficina - caja - factura electronica - consecutivo
[FECHA_EMISION] [datetime] NOT NULL, -- GETDATE()
[CONDICION_VENTA] [varchar](2) NOT NULL, -- ??
[MEDIO_PAGO] [varchar](2) NOT NULL, -- ??
[EMISOR_IDENT_NUM] [varchar](50) NOT NULL, -- PODRIA ESTAR QUEMADO EN EL TRIGGER
[EMISOR_PROVINCIA] [varchar](2) NOT NULL, -- PODRIA ESTAR QUEMADO EN EL TRIGGER
[EMISOR_CANTON] [varchar](3) NOT NULL, -- PODRIA ESTAR QUEMADO EN EL TRIGGER
[EMISOR_DISTRITO] [varchar](3) NOT NULL, -- PODRIA ESTAR QUEMADO EN EL TRIGGER
[EMISOR_OTRAS_SENAS] [varchar](500) NOT NULL, -- PODRIA ESTAR QUEMADO EN EL TRIGGER
[RECEPTOR_NOMBRE] [varchar](100) NULL, -- FACTURA.[CLIENTE]
[RECEPTOR_IDENT_TIPO] [varchar](2) NULL, -- PODRIA ESTAR QUEMADO EN EL TRIGGER
[RECEPTOR_IDENT_NUM] [varchar](2) NULL, -- FACTURA.[CEDULA]
[RESUMEN_COD_MONEDA] [varchar](3) NOT NULL, -- PODRIA ESTAR QUEMADO EN EL TRIGGER
[RESUMEN_TIPO_CAMBIO] [decimal](18, 2) NULL, -- PODRIA ESTAR QUEMADO EN EL TRIGGER
[RESUMEN_TOTAL_MERCANCIAS_GRAVADAS] [decimal](18, 2) NOT NULL, -- FACTURA.[MONTO_TOTAL]
[RESUMEN_TOTAL_MERCANCIAS_EXENTAS] [decimal](18, 2) NOT NULL, -- PODRIA ESTAR QUEMADO EN EL TRIGGER
[RESUMEN_TOTAL_GRAVADO] [decimal](18, 2) NOT NULL, -- FACTURA.[MONTO_TOTAL]
[RESUMEN_TOTAL_EXENTO] [decimal](18, 2) NOT NULL, -- PODRIA ESTAR QUEMADO EN EL TRIGGER
[RESUMEN_TOTAL_VENTA] [decimal](18, 2) NOT NULL, -- FACTURA.[MONTO_TOTAL]
[RESUMEN_TOTAL_DESCUENTOS] [decimal](18, 2) NOT NULL, -- PODRIA ESTAR QUEMADO EN EL TRIGGER
[RESUMEN_TOTAL_VENTA_NETA] [decimal](18, 2) NOT NULL, -- FACUTRA.[MONTO_SUBTOTAL]
[RESUMEN_TOTAL_IMPUESTO] [decimal](18, 2) NOT NULL, -- FACTURA.[IV]
[RESUMEN_TOTAL_COMPROBANTE] [decimal](18, 2) NOT NULL, -- FACTURA.[MONTO_TOTAL]
[NORMATIVA_NUM_RESOLUCION] [varchar](100) NOT NULL, -- PODRIA ESTAR QUEMADO EN EL TRIGGER
[NORMATIVA_FECHA_RESOLUCION] [varchar](100) NOT NULL, -- PODRIA ESTAR QUEMADO EN EL TRIGGER
[OTROS] [varchar](500) NULL, -- PODRIA ESTAR QUEMADO EN EL TRIGGER
[NOTIFY_TO] [varchar](500) NOT NULL, -- FACTURA.[CORREO]
[NOTIFY_FROM] [varchar](500) NOT NULL, -- PODRIA ESTAR QUEMADO EN EL TRIGGER
[PAPEL] [varchar](50) NOT NULL, -- PODRIA ESTAR QUEMADO EN EL TRIGGER
[ERROR] [varchar](max) NULL, -- PODRIA ESTAR QUEMADO EN EL TRIGGER
[ENVIADO_API] [bit] NOT NULL, -- se calcula con trigger