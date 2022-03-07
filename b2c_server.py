#!/usr/bin/env python3
import asyncio
import websockets

clients = {}

class B2Client:
    def __init__(self, ws):
        self.ws = ws

def getClient(ws):
    return clients.get(ws.local_address[0], None)

async def on_connect(ws):
    print(f"{ws.local_address} connected.")
    clients[ws.local_address[0]] = B2Client(ws)

async def on_disconnect(ws, error = False):
    print(f"{ws.local_address} disconnected ({error}).")
    if clients.get(ws.local_address[0], None) != None:
        del clients[ws.local_address[0]] 

async def on_message(ws, msg):
    print(f"recv {ws.local_address}: {msg}")
    print(getClient(ws))

async def client_loop(websocket):
    error = False
    await on_connect(websocket)

    try:
        async for message in websocket:
            await on_message(websocket, message)
            await websocket.send(message)
    except websockets.exceptions.ConnectionClosedError:
        error = True

    await on_disconnect(websocket, error)

async def main():
    async with websockets.serve(client_loop, "", 7790):
        await asyncio.Future()  # run forever

asyncio.run(main())