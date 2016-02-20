import types
from classes.config import NADAV_CONNECTION_STRNIG
from sqlalchemy import *
from datetime import datetime


class ServicesTables():
    server = create_engine(NADAV_CONNECTION_STRNIG, echo=False, convert_unicode=True)

    @staticmethod
    def ensure_table1_table():
        table_name = "table1"
        try:
            table = Table(table_name, MetaData(bind=ServicesTables.server), autoload=True)
        except Exception:
            table = Table(table_name, MetaData(bind=ServicesTables.server),
                          Column("id", Integer, primary_key=True),
                          Column("name", String(255), nullable=False),
                          Column("description", String(255), nullable=False),
                          Column("date_modified", DateTime(timezone=False), nullable=False,
                                 default=datetime.utcnow()),
                          mysql_engine="InnoDB")
            table.create(checkfirst=True)
        return table_name, table

    @staticmethod
    def ensure_logger_table():
        table_name = "log"
        try:
            table = Table(table_name, MetaData(bind=ServicesTables.server), autoload=True)
        except Exception:
            table = Table(table_name, MetaData(bind=ServicesTables.server),
                          Column("id", Integer, primary_key=True),
                          Column("Created", Text, nullable=False),
                          Column("Name", Text, nullable=False),
                          Column("LogLevel", Text, nullable=False),
                          Column("LogLevelName", Text, nullable=False),
                          Column("Message", Text, nullable=False),
                          Column("Args", Text, nullable=False),
                          Column("Module", Text, nullable=False),
                          Column("FuncName", Text, nullable=False),
                          Column("LineNo", Integer, nullable=False),
                          Column("Exception", Text, nullable=False),
                          Column("Process", Text, nullable=False),
                          Column("Thread", Text, nullable=False),
                          Column("ThreadName", Text, nullable=False),
                          mysql_engine="InnoDB")
            table.create(checkfirst=True)
        return table_name, table