from imports.client import ServerClient
from imports.server import MyServer
from api.getImage import NasaAPI
import threading
import sys
import time


def main():
    try:
        serverAddr = ('127.0.0.1', 1340)

        client = ServerClient(serverAddr)
        nasaapi = NasaAPI(True, 'WA8bvHlzEnuQhhPsI0wwSz7C0qph8prAaEdJ6j4H')

        server = MyServer(nasaapi, listening_address=serverAddr)

        serverThread = threading.Thread(target=server.listen)

        serverThread.start()

        client.poll()

    except KeyboardInterrupt:
        sys.stdout.write("\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
