import sys
import socket
import redis

if socket.gethostname() == "MacBookPro":
    sys.path.append("/Users/vovacooper/Work/Nadav/project")
else:
    sys.path.append("/var/www/project")



from providers.nadav_provider import NadavProvider
from classes.logger import logger

from sqlalchemy import text
from datetime import date, datetime, timedelta

class Services:
    def __init__(self, aggregation_date=None):
        self._aggregation_date = aggregation_date
        if not self._aggregation_date:
            self._aggregation_date = date.today()

    def run(self):
        try:
            start_time = datetime.utcnow()
            logger.info("+ Running services")
            provider = NadavProvider()
            provider.run()
            logger.info("- Running services, elapsed time:[{0}]".format(datetime.utcnow() - start_time))
        except Exception, e:
            logger.exception(e)

if __name__ == "__main__":
    service = Services("2016-02-20")
    service.run()
