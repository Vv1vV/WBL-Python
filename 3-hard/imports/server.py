from socket import socket, AF_INET, SOCK_DGRAM
import sys

<<<<<<< Updated upstream
DEFAULT_ADDRESS = ('127.0.0.1', 11113)


class MyServer:
    def __init__(self, NasaAPI, listening_address=DEFAULT_ADDRESS):
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.bind(listening_address)
        self.continueListen = True
        self.NasaAPI = NasaAPI 
        print("Server started. Listening on", listening_address)

=======
DEFAULT_ADDRESS = ('127.0.0.1', 13015)



class MyServer:
    def __init__(self, listening_address=DEFAULT_ADDRESS):
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.bind(listening_address)
        self.continueListen = True
        print("Server started. Listening on", listening_address)    
    
>>>>>>> Stashed changes
    def listen(self):
        try:
            while self.continueListen:
                data, addr = self.socket.recvfrom(1024)
<<<<<<< Updated upstream
                response = bytes(self.act_on(data, addr), "utf-8")
                cmd = str(response.decode())

                if cmd == "exit":
                    self.socket.sendto(
                        bytes("Server is now shutting down", "utf-8"), addr)
                    self.continueListen = False
                elif cmd.split(' ')[0].lower() == 'nasa':
                    string = "\n<----- Attempting To Access Nasa API ----->\n"
                    if len(cmd.split(' ')) > 1:
                        try:
                            arg = int(cmd.split(' ')[1])
                            self.NasaAPI.getDate(arg)
                        except ValueError:
                            self.socket.sendto(
                                bytes(string + "<----- Please Enter a Valid Number ----->", "utf-8"), addr)
                        
                    self.socket.sendto(
                        bytes(string + "<----- Downloading Image now from {0} ----->".format(self.NasaAPI.date), "utf-8"), addr)                    
                    self.NasaAPI.getImage()
                else:
                    self.socket.sendto(response, addr)
=======
                response = bytes(self.act_on(data,addr), "utf-8")
                cmd = str(response.decade())

                if cmd == "exit":
                    self.socket.sendto(
                        bytes("Server is now shutting down"), "utf-8")
                    self.continueListen = False
                else:
                    self.socket.sendto(response, addr)

>>>>>>> Stashed changes
        except KeyboardInterrupt:
            sys.stdout.write("\n")
            sys.exit(0)

<<<<<<< Updated upstream
    def act_on(self, data, addr):
        return data.decode()
=======

    def act_on(self, data, addr):
        return data.decode()
>>>>>>> Stashed changes
