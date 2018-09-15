USE [Moderna]
GO

/****** Object:  Table [dbo].[COMPROBANTE]    Script Date: 9/14/2018 1:12:21 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[COMPROBANTE](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[CLAVE] [varchar](max) NOT NULL,
	[NUMERO_CONSECUTIVO] [varchar](max) NOT NULL,
	[FECHA_EMISION] [datetime] NOT NULL,
	[CONDICION_VENTA] [varchar](2) NOT NULL,
	[MEDIO_PAGO] [varchar](2) NOT NULL,
	[EMISOR_NOMBRE] [varchar](100) NOT NULL,
	[EMISOR_IDENT_TIPO] [varchar](2) NOT NULL,
	[EMISOR_IDENT_NUM] [varchar](50) NOT NULL,
	[EMISOR_NOMBRE_COMERCIAL] [varchar](500) NOT NULL,
	[EMISOR_PROVINCIA] [varchar](2) NOT NULL,
	[EMISOR_CANTON] [varchar](3) NOT NULL,
	[EMISOR_DISTRITO] [varchar](3) NOT NULL,
	[EMISOR_OTRAS_SENAS] [varchar](500) NOT NULL,
	[EMISOR_TEL_COD_PAIS] [int] NOT NULL,
	[EMISOR_TEL_NUM] [varchar](50) NOT NULL,
	[EMISOR_CORREO_ELEC] [varchar](100) NOT NULL,
	[RECEPTOR_NOMBRE] [varchar](100) NULL,
	[RECEPTOR_IDENT_TIPO] [varchar](2) NULL,
	[RECEPTOR_IDENT_NUM] [varchar](2) NULL,
	[RESUMEN_COD_MONEDA] [varchar](3) NOT NULL,
	[RESUMEN_TIPO_CAMBIO] [decimal](18, 2) NULL,
	[RESUMEN_TOTAL_MERCANCIAS_GRAVADAS] [decimal](18, 2) NOT NULL,
	[RESUMEN_TOTAL_MERCANCIAS_EXENTAS] [decimal](18, 2) NOT NULL,
	[RESUMEN_TOTAL_GRAVADO] [decimal](18, 2) NOT NULL,
	[RESUMEN_TOTAL_EXENTO] [decimal](18, 2) NOT NULL,
	[RESUMEN_TOTAL_VENTA] [decimal](18, 2) NOT NULL,
	[RESUMEN_TOTAL_DESCUENTOS] [decimal](18, 2) NOT NULL,
	[RESUMEN_TOTAL_VENTA_NETA] [decimal](18, 2) NOT NULL,
	[RESUMEN_TOTAL_IMPUESTO] [decimal](18, 2) NOT NULL,
	[RESUMEN_TOTAL_COMPROBANTE] [decimal](18, 2) NOT NULL,
	[NORMATIVA_NUM_RESOLUCION] [varchar](100) NOT NULL,
	[NORMATIVA_FECHA_RESOLUCION] [varchar](100) NOT NULL,
	[OTROS] [varchar](500) NULL,
	[AUTH_USUARIO] [varchar](500) NOT NULL,
	[AUTH_PASSWORD] [varchar](max) NOT NULL,
	[AUTH_CERT] [varchar](max) NOT NULL,
	[AUTH_PIN] [varchar](500) NOT NULL,
	[AUTH_DOCUMENTS_ENDPOINT] [varchar](500) NOT NULL,
	[AUTH_API_CLIENT_ID] [varchar](50) NOT NULL,
	[NOTIFY_TO] [varchar](500) NOT NULL,
	[NOTIFY_FROM] [varchar](500) NOT NULL,
	[PAPEL] [varchar](50) NOT NULL,
 CONSTRAINT [PK_COMPROBANTE] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO
