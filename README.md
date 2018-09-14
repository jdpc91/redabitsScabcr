# RS

Description: To be written.

# Installation (either production or development)

Inside a virtual environment do:

```
pip install .
```

# Scripts that use RS module

They go into `bin/`, do `pip install .` to install RS with all its dependencies and develop the script normally.

# Starting MSSQL with Docker on GNU/Linux or Windows

If you don't have MSSQL installed on your Windows machine or currently just have GNU/Linux, and you have Docker and Docker compose installed you can use `python setup.py docker_start` which will start a MSSQL docker image exposing the service at the port `1433`, you can also use `python setup.py docker_stop` to stop the docker container.


# Restore backup for development

On `/var` create a directory called `opt/mssql/db`, place the `MODERNA13.BAK` file under `/var/opt/mssql` and restore the database with the following command (**this only works for MSSQL running as a Docker image under GNU/Linux**):

```
sqlcmd -S localhost -U SA -P u2ykHVe3XMSPzvL9 -Q "RESTORE DATABASE TESTING FROM DISK = '/var/mssql/MODERNA13.BAK' WITH MOVE \"CARNES\" TO \"/var/mssql/db/CARNES.mdf\", MOVE \"CARNES_log\" TO \"/var/mssql/db/CARNES.ldf\""
```

The name of the database will be `TESTING`.

# For help

Do the following

```
python setup.py --help-commands
```
