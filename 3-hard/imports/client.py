from sockets.python3.client import Client


class ServerClient:
    def __init__(self, server):
        self.client = Client()
        self.server = server

    def poll(self):
        userInput = ''

        while userInput != 'exit':
            userInput = input(
            "Server message (use exit to leave) > ")
            response, addr = self.client.poll_server(
                userInput, server=self.server)
            print(response, addr)
            self.reInitConnection()

    def reInitConnection(self):
        self.client = Client()
