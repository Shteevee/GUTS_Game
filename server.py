from lib.Mastermind import *
import threading
from time import gmtime, strftime
import traceback
import settings

class GameServer(MastermindServerTCP):
    def __init__(self):
        MastermindServerTCP.__init__(self,
                                    settings.time_server_refresh,
                                    settings.time_connection_refresh,
                                    settings.time_connection_timeout)
        self.log = [None] * settings.scrollback
        self.mutex = threading.Lock()
        self.driver_connected = False
        self.navigator_connected = False

    def log_message(self, msg):
        timestamp = strftime("%H:%M:%S",gmtime())
        self.mutex.acquire()
        self.log = self.log[1:] + [timestamp + " | " + msg]
        self.mutex.release()
        print(timestamp + " | " + msg)

    def callback_connect(self):
        self.log_message("Server connected")
        return super(GameServer, self).callback_connect()

    def callback_disconnect(self):
        self.log_message("Server disconnected")
        return super(GameServer, self).callback_disconnect()

    def callback_connect_client(self, client):
        self.log_message(str(client.address) + " has connected")
        return super(GameServer, self).callback_connect_client(client)

    def callback_disconnect_client(self, client):
        self.log_message(str(client.address) + " has disconnected")
        return super(GameServer, self).callback_disconnect_client(client)

    def callback_client_handle(self, client, data):
        self.log("Server received " + str(data[0]))
        return super(GameServer, self).callback_client_handle(client, data)
        #position = data[0]
        #self.log_message(position)

def start_server():
    server = GameServer()
    try:
        server.connect(settings.ip, settings.port)
    except:
        print("Server failed to connect")

    server.accepting_allow()
    return server

def stop_server(server):
    server.accepting_disallow()
    server.disconnect_clients()
    server.disconnect()

try:
    get_input = raw_input
except:
    get_input = input

def main():
    print("=================================================")
    print("=             Don't Get Lost v1.0               =")
    print("=================================================")
    print()
    print("Starting server . . .")
    server = start_server()
    print()
    print("Type 'exit' to stop the server")

    running = True
    while running:
        command = get_input(">>> ")

        if command == "exit":
            running = False

    if server != None:
        stop_server(server)

if __name__ == "__main__":
    try:
        main()
    except:
        traceback.print_exc()
        get_input()
