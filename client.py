from lib.Mastermind import *
import settings
import gameMap
import traceback

class GameClient(MastermindClientTCP):
    def __init__(self):
        MastermindClientTCP.__init__(self,
                                    settings.timeout_connect,
                                    settings.timeout_receive)

    def connect(self):
        print("Client connecting on \"" + settings.ip +
                "\", port " + str(settings.port) + " . . .")

        try:
            super(GameClient, self).connect(settings.ip, settings.port)
        except MastermindError:
            print("Server is not running!")

    def wait_for_data(self):
        return super(GameClient, self).receive(True)

    def ask_which_map(self):
        return super(GameClient, self).send("which_map")

    def ask_for_map(self):
        return super(GameClient, self).send("send_map")

    def get_metrics(self):
        return super(GameClient, self).send("get_metrics")

    def send_metrics(self, x, y, direction):
        return super(GameClient, self).send((x, y, direction))

def run(game_loop):
    client = GameClient()
    client.connect()
    client.ask_which_map()
    map_file = client.wait_for_data()

    try:
        open(map_file, "r")
    except:
        client.ask_for_map()
        map_data = client.wait_for_data()
        open(map_file, "wb").write(map_data).close()

    game_map = gameMap.GameMap(map_file)

    try:
        game_loop(client, game_map)
        client.disconnect()
    except:
        traceback.print_exc()
        client.disconnect()
