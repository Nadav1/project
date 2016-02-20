import sys
import socket
import redis

if socket.gethostname() == "MacBookPro":
    sys.path.append("/Users/vovacooper/Work/Nadav/project")
else:
    sys.path.append("/var/www/project")

from services.services import Services


if __name__ == "__main__":
    service = Services("2016-02-20")
    service.run()


