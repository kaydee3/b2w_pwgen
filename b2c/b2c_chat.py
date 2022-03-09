import asyncio
import dearpygui.dearpygui as dpg
import websocket
import rel

rel.safe_read()

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")

import aioconsole

async def main_loop():
    line = await aioconsole.ainput('Is this your line? ')
    print(line)
# If this file is the main file, and not a library, execute main function loop
if __name__ == "__main__":
    
    ws = websocket.WebSocketApp("wss://82.6.205.72:7790",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)
    asyncio.run(main_loop())
    ws.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()
