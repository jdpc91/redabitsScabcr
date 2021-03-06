Changelog
=========


0.3 (2018-09-19)
----------------

Changes
~~~~~~~
- Show basic information for class instance of Factura. [Jorge Araya
  Navarro]

Fix
~~~
- Update Factura counter during testing. [Jorge Araya Navarro]

  Avoid sending repeated voucher number to Hacienda


0.2 (2018-09-19)
----------------

Changes
~~~~~~~
- Bump version. [Jorge Araya Navarro]
- Add Impuesto only if there is some. [Jorge Araya Navarro]
- Update RESUMEN_* columns in Comprobante model. [Jorge Araya Navarro]

  In accordance with the following JSON example:

      "ResumenFactura":
  	{
  		"CodigoMoneda":"",//USD para dolares, CRC para colones. Si es null por defecto es CRC
  		"TipoCambio":"",//Obligatorio si "CodigoMoneda" != CRC
  		"TotalMercanciasGravadas":2654.88,//suma de "SubTotal" de las lineas que tengan "Impuesto"
  		"TotalMercanciasExentas":0,//suma de "SubTotal" de las lineas que no tengan "Impuesto"
  		"TotalGravado":2654.88,//igual que "TotalMercanciasGravadas" en este proyecto
  		"TotalExento":0,//igual que "TotalMercanciasExentas" en este proyecto
  		"TotalVenta":2654.88,//"TotalGravado" + "TotalExento"
  		"TotalDescuentos":0,//suma de "MontoDescuento" de las lineas que lo tengan
  		"TotalVentaNeta":2654.88,//"TotalVenta" - "TotalDescuentos"
  		"TotalImpuesto":345.1344,//suma de "Monto" de todos los "Impuesto"
  		"TotalComprobante":3000.0144//"TotalVentaNeta" + "TotalImpuesto"
  	}
- Raise error in status 200 with bogus content. [Jorge Araya Navarro]

  Prevents quirks from the API by ensuring that clave is a long string of digits.

Fix
~~~
- Fix wrong access to dict inside list. [Jorge Araya Navarro]
- Include missing field. [Jorge Araya Navarro]
- Use IV column for taxes instead of hardcoded amount. [Jorge Araya
  Navarro]
- Check if clave is form out of digits. [Jorge Araya Navarro]

  Avoid total failure of the app
- Use same URL base for testing. [Jorge Araya Navarro]
- Use different URL base for sandbox. [Jorge Araya Navarro]
- Remove unused imports. [Jorge Araya Navarro]
- Add field as a list of dicts. [Jorge Araya Navarro]
- Add missing field and correction of typos. [Jorge Araya Navarro]
- Fix misnamed field in payload. [Jorge Araya Navarro]

Other
~~~~~
- Fixing the conversion of the num_factura. [Dennis Hernández]


0.1 (2018-09-18)
----------------

New
~~~
- Change in README files. [Jorge Araya Navarro]
- Update Comprobante state when receipt is received by API. [Jorge Araya
  Navarro]
- Add executable script. [Jorge Araya Navarro]

  This script does the job of sending all receipts in batches.
- Add model for table, functions and new tests. [Jorge Araya Navarro]

  - https://ptpb.pw/GaBt
- Implementa modelo para varias tablas. [Jorge Araya Navarro]

  Las tablas afectadas son `FACTURAS`, `HISTORICO_MOV`, `COMPROBANTE` y `COMPROBANTE_LINEA_DETALLE`
- Provide object for connection with MSSQL database. [Jorge Araya
  Navarro]

  `DATABASE_URL` is an environment variable which holds the information required to connect with a
  database server.
- Add Python dependencies. [Jorge Araya Navarro]
- Change docker service allowing database restore. [Jorge Araya Navarro]

  Binding directories allow for the Docker service to reach the backup file
- Enable usage of Docker for development. [Jorge Araya Navarro]

  MSSQL image for docker can be use for a zero-conf MSSQL database
- Add README. [Jorge Araya Navarro]
- Add setup.py. [Jorge Araya Navarro]
- Aplica directiva de archivos ignorados para Git. [Jorge Araya Navarro]

Changes
~~~~~~~
- Format source code and remove models. [Jorge Araya Navarro]
- Format source code with Black. [Jorge Araya Navarro]

  - https://github.com/ambv/black
- Borra prueba unitaria. [Jorge Araya Navarro]
- Factura model generate the purchase details. [Jorge Araya Navarro]
- Remove ComprobanteDetalle model. [Jorge Araya Navarro]
- Several changes for models. [Jorge Araya Navarro]
- Set Clave as returned by Daniel's API. [Jorge Araya Navarro]
- Add Emisor data from API request. [Jorge Araya Navarro]

  - commit b3f256f70bb83558ab5c0f119b8d3ae7429cdcd1
  - issue #5
- Update integration test. [Jorge Araya Navarro]
- Ensure field has content. [Jorge Araya Navarro]
- Generate several invoices for testing. [Jorge Araya Navarro]

  Boilerplate data from the database that help with integration tests
- Add debugging information for API consumer. [Jorge Araya Navarro]

  Sometimes the API consumed does not return expected responses
- Establece relacion entre tablas. [Jorge Araya Navarro]

  Tablas afectadas son `COMPROBANTE` y `COMPROBANTE_LINEA_DETALLE`, la relación es *one-to-many*
  siendo `COMPROBANTE` el padre.

  - https://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#one-to-many
- Explain where scripts should go. [Jorge Araya Navarro]

Fix
~~~
- Fix length of field in table Comprobante. [Jorge Araya Navarro]

  - fixes issue #6
- Fix column length and add missing fields. [Jorge Araya Navarro]
- Return requests response. [Jorge Araya Navarro]
- Ensure error are raised if `DetallesServicio` is empty. [Jorge Araya
  Navarro]
- Remove several fields from model. [Jorge Araya Navarro]

  They do not exists in the new SQL scripts

  - fix issue #4
- Fix boilerplate data generator. [Jorge Araya Navarro]
- Fix wrong syntax. [Jorge Araya Navarro]

  - fixes issue #2
- Arregla argumento posicional luego de argumento nombrado. [Jorge Araya
  Navarro]

  ```
      Integer, name='COMPROBANTE_ID', ForeignKey('COMPROBANTE.ID'))
                                     ^
  SyntaxError: positional argument follows keyword argument
  ```
- Use correct dependency versions. [Jorge Araya Navarro]
- Move the directory bind outside project directory. [Jorge Araya
  Navarro]

  There is interference with `pip install` because the file permission of the database data under `data/db/`
- Include missing directory. [Jorge Araya Navarro]

Other
~~~~~
- Removing NOT NULL. [Dennis Hernández]
- Deleting linea_detalle and adding NUM_FACTURA to Comprobante.
  [djhvscf]
- Clave null to not null. [Dennis Hernández]
- Deleting where clause. [djhvscf]
- Merge branch 'master' of https://github.com/jdpc91/redabitsScabcr.
  [djhvscf]
- Merge branch 'master' of github.com:jdpc91/redabitsScabcr. [Jorge
  Araya Navarro]
- Fix issue with comma. [djhvscf]
- Fixing comprobantes_electronicos variable. [djhvscf]
- Updating mapping. [djhvscf]
- Adding EMISOR_IDENT_NUM with value. [djhvscf]
- Adding EMISOR_IDENT_NUM column. [djhvscf]
- Merge branch 'master' of https://github.com/jdpc91/redabitsScabcr.
  [djhvscf]
- Merge branch 'master' of github.com:jdpc91/redabitsScabcr. [Jorge
  Araya Navarro]
- Adding correo_emisor. [djhvscf]
- Deleting unused columns. [djhvscf]
- Fixing hardcoded values with select statement. [djhvscf]
- Adding 0_Drop_tables_and_triggers.sql. [djhvscf]
- Adding validation IF EXISTS THEN DROP. [djhvscf]
- Fix issue with trigger where insert or update statement is executed.
  [djhvscf]
- Adding ENVIADO_API column. [djhvscf]
- Adding Enviado_Api column. [djhvscf]
- Adding docs about tables. [djhvscf]
- Adding create trigger comprobante. [djhvscf]
- Adding order of execution. [djhvscf]
- Adding create_tabla_comprobante_audit. [djhvscf]
- Adding create tabla Comprobante_Linea_Detalle. [djhvscf]
- Create tabla comprobante. [djhvscf]
- Adding alter table statement for Factura table. [djhvscf]


