Changelog
=========


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


