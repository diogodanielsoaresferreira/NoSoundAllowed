import asyncio
import websockets
import json
import time
from random import *


s_id = input("Sensor id: ")

async def send_value(s_id):
    async with websockets.connect(
            'ws://localhost:8000/ws/values/') as websocket:
        

        await websocket.send(json.dumps({
                    'id': s_id,
                    'type': "NO",
                    'value': float(input("Noise value: ")),
                }))


        await websocket.send(json.dumps({
                    'id': s_id,
                    'type': "TE",
                    'value': float(input("Temperature value: ")),
                }))


while(True):
	asyncio.get_event_loop().run_until_complete(send_value(s_id))
	
	time.sleep(1)