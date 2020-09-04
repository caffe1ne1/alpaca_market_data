import requests
import websocket
import config
import json

# unlimited stream of market data for requested stocks


def on_open(ws):
    print("opened")
    auth_data = config.Header
    ws.send(json.dumps(auth_data))

    stonk_request = {
        "action": "listen",
        "data": {"streams": ["T.SPY", "Q.SPY", "AM.SPY"]
                 }
    }
    ws.send(json.dumps(stonk_request))


def on_message(ws, message):
    print(message)


def on_close(ws):
    print("closed connection")


socket = "wss://data.alpaca.markets/stream"
# open a new websocket, connecting to socket address, give it our
# instructions for events
ws = websocket.WebSocketApp(socket, on_open=on_open,
                            on_message=on_message, on_close=on_close)
ws.run_forever()
