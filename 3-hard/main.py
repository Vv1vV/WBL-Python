<<<<<<< Updated upstream
<<<<<<< Updated upstream

def main():
    print("Hello World")
=======
from imports.client import ServerClient
from imports.server import MyServer
from api.getimage import NasaAPI
import threading
import sys


def main():
    try:
        serverAddr = ('127.0.0.1', 13021)

        client = ServerClient(serverAddr)
        nasaapi = NasaAPI(True, 'Q57tkvzlvAtlzk7T2Giv8dZq6e97r1VjuF9cESzW')
        server = MyServer(nasaapi, listening_address=serverAddr)

        serverThread = threading.Thread(target=server.listen)

=======
from imports.client import ServerClient
from imports.server import MyServer
import threading
import sys


def main():
    try:    
        serverAddr = ('127.0.0.1', 13005)

        client = ServerClient(serverAddr)
        server = MyServer(listening_address=serverAddr)
    
        serverThread = threading.Thread(target=server.listen)
    
>>>>>>> Stashed changes
        serverThread.start()

        client.poll()
    except KeyboardInterrupt:
<<<<<<< Updated upstream
        sys.stdout.write("\n")
        sys.exit(0)
>>>>>>> Stashed changes
=======
        sys.stdout.write("\n")       
        sys.exit(0)
    
>>>>>>> Stashed changes


if __name__ == "__main__":
    main()
