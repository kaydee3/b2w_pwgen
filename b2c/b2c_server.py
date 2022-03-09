#!/usr/bin/env python3
# Import Python's asyncio library to enable concurrency
import asyncio
# Import websockets, the protocol we're using for the connection 
import websockets
# Import bashlib, for base level encryption on stored passwords
import hashlib

# Defining a dictionary where we will store references to each client that connects.
clients = {}
history = []

# Return a hash of a given text value, e.g. an encrypted string that can't be converted back to original.
def hash(msg):
    return hashlib.sha256(bytes(msg, "utf-8")).hexdigest()

# Event for when a client connects.
async def on_connect(ws):
    # Show in server log that a client has connected.
    print(f"{ws.local_address} {ws.id} connected.")
    
    # Store a reference to the socket connection object in our clients dictionary
    clients[str(ws.id)] = ws

    # Send the connected client their unique ID that the client will use to identify itself
    await ws.send(f"/ID/{ws.id}/")

    # Tell all clients that this client has connected
    for id, client in clients.items():
        await client.send(f"/CONNECT/{ws.id}/")

    
# Event for when a client disconnects.
async def on_disconnect(ws, error = False):
    print(f"{ws.local_address} disconnected ({error}).")

    # Remove this client from the dict
    if clients.get(str(ws.id), None) != None:
        del clients[str(ws.id)] 

    # Announce the departure
    for id, client in clients.items():
        await client.send(f"/DISCONNECT/{ws.id}/");

# Event for recieving a message from the client
async def on_message(ws, msg):
    global history
    
    print(f"MESSAGE {ws.id}: {msg}")

    if msg == "/REQUEST_HISTORY/":
        his = '|'.join(history)
        ln = f"/HIST/{his}/"
        print(ln)
        await ws.send(ln)

    if msg.startswith("/MSG/"):
        history.append(msg)
    print("New history")
    print(history)
    # Dispatch message to all clients except sender
    for id, client in clients.items():
        if ws != client: await client.send(msg)

# Main loop of the server
async def client_loop(websocket):
    # Define an error check variable
    error = False

    # Run our connect event
    await on_connect(websocket)

    # The script halts here, and waits for messages until they disconnect
    try:
        # Async, allowing this loop to run without interrupting other loops also running
        # Essentially allowing multiple copies of this to run at the same time, one for each client.
        async for message in websocket:
            # Send it to our message event.
            await on_message(websocket, message)

            # Echo it back to the sender
            await websocket.send(message)
    except websockets.exceptions.ConnectionClosedError:
        # We've errored, so set this to true
        error = True

    # Once the client disconnects, the previous loop ends, allowing this function to now run
    await on_disconnect(websocket, error)

async def main():
    # Starting our server.
    # Parameter 1: the function to use for the client that connects
    # Parameter 2: leave blank
    # Parameter 3: the servers port

    async with websockets.serve(client_loop, "", 7790):
        await asyncio.Future()  # run forever

asyncio.run(main())