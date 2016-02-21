import requests
from classes.logger import logger
from classes.mysql_tables import ServicesTables
from datetime import datetime

from classes.logger import logger




import requests
import time
import re
import json
from sqlalchemy import *
from datetime import datetime


class NadavProvider:
    def __init__(self):
        self._bla = None

    def run(self):
        self._read_html()
        self._insert_mysql_example()
        self._select_mysql_example()
        self._update_mysql_example()

        return

    def _read_html(self):
        r = requests.get('https://www.google.com')
        r.status_code


    def _insert_mysql_example(self):
        table_name, table = ServicesTables.ensure_table1_table()

        data = [{
            "name": "nadav",
            "description": "gandonaa",
            "date_created": datetime.utcnow()
        }, {
            "name": "nadav1",
            "description": "gandon1",
            "date_created": datetime.utcnow()
        }, {
            "name": "nadav2",
            "description": "gandon2",
            "date_created": datetime.utcnow()
        }, {
            "name": "nadav3",
            "description": "gandon3",
            "date_created": datetime.utcnow()
        }, {
            "name": "nadav4",
            "description": "gandon4",
            "date_created": datetime.utcnow()
        }]

        for d in data:
            table.insert().values(d).execute()

        return

    def _select_mysql_example(self):
        table_name, table = ServicesTables.ensure_table1_table()

        sql = text(" SELECT * FROM {0} where name=:name".format(table_name))
        db_result = ServicesTables.server.execute(sql, name="nadav")

        db_result = list(db_result)
        for d in db_result:
            print d

        table_name, table = ServicesTables.ensure_table1_table()

        sql = text(" SELECT * FROM {0}".format(table_name))
        db_result = ServicesTables.server.execute(sql)

        db_result = list(db_result)
        for d in db_result:
            print d
        return

    def _update_mysql_example(self):
        table_name, table = ServicesTables.ensure_table1_table()
        sql = text(
                " UPDATE {0} "
                " SET description=:description".format(table_name))
        ServicesTables.server.execute(sql, description=" ha ha ha ha h ah")
        return


if __name__ == "__main__":
    service = NadavProvider()
    service.run()


