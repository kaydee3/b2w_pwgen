import websocket

ws = websocket.WebSocket()
ws.connect("ws://82.6.205.72:7790")

def main():
    while True:
        i = input(">_ ")

        if i == ".q": 
            ws.close()
            return

        ws.send(i)
        print(ws.recv())

main()
