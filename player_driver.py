from lib.Mastermind import *
import settings

def start_driver_client():
    client = MastermindClientTCP(settings.timeout_connect,
                                settings.timeout_receive)

    try:
        print("Client connecting on \""+settings.ip+"\", port "+str(settings.port)+" . . .")
        client.connect(settings.ip,settings.port)
    except MastermindError:
        print("No server found; starting server!")
        # server = chat_server.ServerChat()
        # server.connect(server_ip,port)
        # server.accepting_allow()
        #
        # print("Client connecting on \""+client_ip+"\", port "+str(port)+" . . .")
        # client.connect(client_ip,port)
    print("Client connected!")
    client.send("WTF", None)
    client.disconnect()
