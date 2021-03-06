USE [Moderna]
GO

INSERT INTO COMPROBANTE
	   ([CLAVE]
	   ,[NUM_FACTURA]
       ,[NUMERO_CONSECUTIVO]
       ,[FECHA_EMISION]
       ,[CONDICION_VENTA]
       ,[MEDIO_PAGO]
	   ,[EMISOR_IDENT_NUM]
       ,[EMISOR_PROVINCIA]
       ,[EMISOR_CANTON]
       ,[EMISOR_DISTRITO]
       ,[EMISOR_OTRAS_SENAS]
       ,[RECEPTOR_NOMBRE]
       ,[RECEPTOR_IDENT_TIPO]
       ,[RECEPTOR_IDENT_NUM]
       ,[RESUMEN_COD_MONEDA]
       ,[RESUMEN_TIPO_CAMBIO]
       ,[RESUMEN_TOTAL_MERCANCIAS_GRAVADAS]
       ,[RESUMEN_TOTAL_MERCANCIAS_EXENTAS]
       ,[RESUMEN_TOTAL_GRAVADO]
       ,[RESUMEN_TOTAL_EXENTO]
       ,[RESUMEN_TOTAL_VENTA]
       ,[RESUMEN_TOTAL_DESCUENTOS]
       ,[RESUMEN_TOTAL_VENTA_NETA]
       ,[RESUMEN_TOTAL_IMPUESTO]
       ,[RESUMEN_TOTAL_COMPROBANTE]
       ,[REFERENCIA_NUMERO]
       ,[NORMATIVA_NUM_RESOLUCION]
       ,[NORMATIVA_FECHA_RESOLUCION]
       ,[OTROS]
       ,[NOTIFY_TO]
       ,[NOTIFY_FROM]
       ,[PAPEL]
       ,[ERROR]
       ,[ENVIADO_API])
(SELECT
FOLIOMH
	,NUM_FACTURA
	,'00100001' + 
		(CASE TIPO 
			WHEN 'F' THEN '01' 
			WHEN 'D' THEN '02' 
			ELSE '03' 
		END) + 
		(CASE 
			WHEN NUM_FACTURA = 9999999999 THEN '0000000001' 
			ELSE RIGHT(REPLICATE('0', 10) + CONVERT(VARCHAR(10), NUM_FACTURA), 10) 
		END)
	,GETDATE()
	,'01'
	,(CASE WHEN [MONTO_TARJETA] IS NULL THEN '01' ELSE '02' END)
	,(SELECT TOP 1 CONVERT(VARCHAR(50), DECRYPTBYPASSPHRASE('scab456', EMISOR)) FROM [dbo].[POS])
	,(SELECT TOP 1 [provincia] FROM [dbo].[POS])
	,(SELECT TOP 1 [CANTON] FROM [dbo].[POS]) 
	,(SELECT TOP 1 [DISTRITO] FROM [dbo].[POS]) 
	,(SELECT TOP 1 [OTRAS_SENAS] FROM [dbo].[POS])
	,CLIENTE
	,'01'
	,CEDULA
	,'CRC'
	,585
	,MONTO_TOTAL
	,0
	,MONTO_TOTAL
	,0
	,MONTO_TOTAL
	,0
	,SUBTOTAL
	,IV
	,MONTO_TOTAL
	,RESPUESTA_HACIENDA
	,'DGT-R-48-2016'
	,'20-02-2017 13:22:22'
	,NULL
	,CORREO
	,(SELECT TOP 1 [CORREO_EMISOR] FROM [dbo].[POS])
	,(SELECT TOP 1 [TIPO_PAPEL] FROM [dbo].[POS])
	,MENSAJE_ERROR
	,(CASE WHEN [FOLIOMH] NOT LIKE '506%' OR FOLIOMH IS NULL THEN 0 ELSE 1 END)
FROM FACTURAS WHERE FOLIOMH NOT LIKE '506%' OR FOLIOMH IS NULL)

GO
