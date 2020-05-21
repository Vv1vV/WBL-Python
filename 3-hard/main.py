from imports.client import ServerClient
from imports.server import MyServer
import threading
import sys


def main():
    try:
        serverAddr = ('127.0.0.1', 1337)

        client = ServerClient(serverAddr)
        server = MyServer(listening_address=serverAddr)

        serverThread = threading.Thread(target=server.listen)

        serverThread.start()

        client.poll()
    except KeyboardInterrupt:
        sys.stdout.write("\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
