#!/usr/bin/env python3
import asyncio
import enum
import websockets
import hashlib

clients = {}

 
def hash(msg):
    return hashlib.sha256(bytes(msg, "utf-8")).hexdigest()

async def on_connect(ws):
    print(f"{ws.local_address} {ws.id} connected.")
    clients[str(ws.id)] = ws
    for id, client in clients.items():
        await client.send(f"{ws.id} connected.")

    

async def on_disconnect(ws, error = False):
    print(f"{ws.local_address} disconnected ({error}).")
    if clients.get(str(ws.id), None) != None:
        del clients[str(ws.id)] 
    for id, client in clients.items():
        await client.send(f"{ws.id} left.")

async def on_message(ws, msg):
    print(f"recv {ws.id}: {msg}")
    for id, client in clients.items():
        await client.send(msg)

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