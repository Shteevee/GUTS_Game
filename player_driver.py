from lib.Mastermind import *
import settings
import traceback
import gameMap

class DriverClient(MastermindClientTCP):
    def __init__(self):
        MastermindClientTCP.__init__(self,
                                    settings.timeout_connect,
                                    settings.timeout_receive)

    def connect(self):
        print("Client connecting on \"" + settings.ip +
                "\", port " + str(settings.port) + " . . .")

        try:
            super(DriverClient, self).connect(settings.ip, settings.port)
        except MastermindError:
            print("Server is not running!")

    def wait_for_data(self):
        return super(DriverClient, self).receive(True)

    def ask_which_map(self):
        return super(DriverClient, self).send("which_map")

    def ask_for_map(self):
        return super(DriverClient, self).send("send_map")

    def disconnect(self):
        return super(DriverClient, self).disconnect()

def main():
    driver = DriverClient()
    driver.connect()
    driver.ask_which_map()
    map_file = driver.wait_for_data()

    try:
        open(map_file, "r")
    except:
        driver.ask_for_map()
        map_data = driver.wait_for_data()
        open(map_file, "wb").write(map_data).close()

    game_map = gameMap.GameMap(map_file)
    driver.disconnect()

if __name__ == "__main__":
    try:
        main()
    except:
        traceback.print_exc()
        input()
