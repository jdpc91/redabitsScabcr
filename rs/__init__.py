#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DEV_DATABASE_URL = ("mssql+pyodbc://sa:u2ykHVe3XMSPzvL9@127.0.0.1:1433/"
                    "TESTING?driver=ODBC+Driver+17+for+SQL+Server")

engine = create_engine(getenv('DATABASE_URL', DEV_DATABASE_URL), echo=False)
# You import `session` for doing calls to the database, more about the session
# object here:
# https://docs.sqlalchemy.org/en/latest/orm/session_api.html#session-and-sessionmaker
session = sessionmaker(bind=engine)()
