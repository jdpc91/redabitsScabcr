# RS

Envía comprobantes de las facturas insertadas en la base de datos a la API de facturas de REDABITS.

# Instalación

Primero lea esta [guía de instalación de ODBC para Windows](https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/step-1-configure-development-environment-for-pyodbc-python-development?view=sql-server-2017) hasta el punto 3. Luego de descargar el repositorio se ejecuta `pip` para instalar el paquete con todas sus dependencias:

```
pip install .
```

# Variables de entorno

- `DEBUG`: Si esta establecido (con cualquier valor diferente a una cadena vacía) usa una configuración adecuada para pruebas. **No se meten datos falsos a ninguna base de datos durante la ejecución**. Para usar valores de producción esta variable de entorno **no** debe ser establecida, además, debe correr el script con la bandera `--production`.
- `DATABASE_URL`: Indica la URL o el DSN de la base de datos MSSQL. El formato para DSN tiene que ser `mssql+pyodbc://<username>:<password>@<dsnname>`, para conexion por URL el formato debe ser `mssql+pyodbc://<username>:<password>@<host>:<port>/<databasename>?driver=<SQL+Server+Native+Client+XX.YY>` el SQL Server driver puede variar, para conocer el valor correcto se puede usar el siguiente comando desde la linea de comandos:

```
python -c 'import pyodbc; print(pyodbc.drivers())'
```

# Como usar

Simplemente ejecute `rsb --production` para una ejecución con configuración de producción.

# Pruebas de integración (CAMBIOS DESTRUCTIVOS EN LA BASE DE DATOS)

**Las pruebas unitarias deben realizarse en una base de datos que no sea del cliente**. Dentro del proyecto puede ejecutar `python setup.py test`.
