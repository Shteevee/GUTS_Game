from lib.Mastermind import *
from time import localtime, strftime
import traceback
import settings
import gameMap

class GameServer(MastermindServerTCP):
    def __init__(self):
        MastermindServerTCP.__init__(self,
                                    settings.time_server_refresh,
                                    settings.time_connection_refresh,
                                    settings.time_connection_timeout)
        self.driver_connected = False
        self.navigator_connected = False
        self.car_position = (settings.car_x, settings.car_y)

    def log_message(self, msg):
        timestamp = strftime("%H:%M:%S", localtime())
        print()
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
        if data == "which_map":
            self.log_message(str(client.address) + " asked which map")
            self.callback_client_send(client, settings.game_map)

        elif data == "send_map":
            self.log_message(str(client.address) + " asked for the map")
            map_data = open(settings.game_map, "rb").read()
            self.callback_client_send(client, map_data)

        elif data == "get_position":
            self.log_message(str(client.address) + " asked for car position, sending " + str(self.car_position))
            self.callback_client_send(client, self.car_position)

        elif type(data) == tuple:
            self.log_message(str(client.address) + " sent car position " + str(data))
            self.car_position = data
        return super(GameServer, self).callback_client_handle(client, data)

    def callback_client_send(self, client, data):
        self.log_message("Sending data to " + str(client.address))
        return super(GameServer, self).callback_client_send(client, data)

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
    print("Type 'exit' to stop the server")

    server = GameServer()
    try:
        server.connect(settings.ip, settings.port)
    except:
        server.log_message("Server failed to connect")
    server.accepting_allow()

    running = True
    while running:
        command = get_input(">>> ")

        if command == "exit":
            running = False

    if server != None:
        server.accepting_disallow()
        server.disconnect_clients()
        server.disconnect()

if __name__ == "__main__":
    try:
        main()
    except:
        traceback.print_exc()
        get_input()
