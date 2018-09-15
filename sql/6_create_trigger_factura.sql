USE [Moderna]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET NOCOUNT ON
GO

CREATE TRIGGER [dbo].[INSERT_COMPROBANTE] ON [dbo].[FACTURAS]
AFTER INSERT
AS

DECLARE @p1 TABLE (col VARCHAR(30))

DECLARE @Prefix_Num_Consecutivo varchar(max)
DECLARE @Num_Consecutivo varchar(max)
DECLARE @Cantidad_Comprobantes int

SET @Cantidad_Comprobantes = (SELECT COUNT(DISTINCT CLAVE) FROM [dbo].[COMPROBANTE])
SET @Prefix_Num_Consecutivo = '0010000101'

IF @Cantidad_Comprobantes = 9999999999
	SET @Num_Consecutivo = '0000000001';
ELSE
	SET @Num_Consecutivo = RIGHT(REPLICATE('0', 10) + @Cantidad_Comprobantes, 10);


INSERT INTO COMPROBANTE
			([CLAVE]
           ,[NUMERO_CONSECUTIVO]
           ,[FECHA_EMISION]
           ,[CONDICION_VENTA]
           ,[MEDIO_PAGO]
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
           ,[NORMATIVA_NUM_RESOLUCION]
           ,[NORMATIVA_FECHA_RESOLUCION]
           ,[OTROS]
           ,[NOTIFY_TO]
           ,[NOTIFY_FROM]
           ,[PAPEL]
           ,[ERROR]
           ,[ENVIADO_API])
(SELECT
	FOLIOMH,
	CONCAT(@Prefix_Num_Consecutivo, @Num_Consecutivo),
	GETDATE(),
	'01',
	IIF ([MONTO_TARJETA] IS NULL OR [MONTO_TARJETA] = 0, '01', '02'),
	(SELECT [provincia] FROM [dbo].[POS] WHERE [COD_POS] = 'TIENDA'),
	(SELECT [CANTON] FROM [dbo].[POS] WHERE [COD_POS] = 'TIENDA'), 
	(SELECT [DISTRITO] FROM [dbo].[POS] WHERE [COD_POS] = 'TIENDA'), 
	(SELECT [OTRAS_SENAS] FROM [dbo].[POS] WHERE [COD_POS] = 'TIENDA')
	CLIENTE,
	'01',
	CEDULA,
	'CRC',
	585,
	MONTO_TOTAL,
	0,
	MONTO_TOTAL,
	0,
	MONTO_TOTAL,
	0,
	SUBTOTAL,
	IV,
	MONTO_TOTAL,
	'DGT-R-48-2016',
	'20-02-2017 13:22:22',
	NULL,
	CORREO,
	'reportes@scabcr.com',
	'tiquete',
	MENSAJE_ERROR,
	IIF (FOLIOMH IS NULL OR FOLIOMH = '', 0, 1)
FROM 
	inserted)

SELECT 
	* 
FROM 
	@p1

GO


