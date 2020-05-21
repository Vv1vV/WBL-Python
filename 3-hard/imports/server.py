from socket import socket, AF_INET, SOCK_DGRAM
import sys

DEFAULT_ADDRESS = ('127.0.0.1', 11113)


class MyServer:
    def __init__(self, listening_address=DEFAULT_ADDRESS):
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.bind(listening_address)
        self.continueListen = True
        print("Server started. Listening on", listening_address)

    def listen(self):
        try:
            while self.continueListen:
                data, addr = self.socket.recvfrom(1024)
                response = bytes(self.act_on(data, addr), "utf-8")
                cmd = str(response.decode())

                if cmd == "exit":
                    self.socket.sendto(
                        bytes("Server is now shutting down", "utf-8"), addr)
                    self.continueListen = False
                else:
                    self.socket.sendto(response, addr)
        except KeyboardInterrupt:
            sys.stdout.write("\n")
            sys.exit(0)

    def act_on(self, data, addr):
        return data.decode()
