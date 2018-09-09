import asyncio
import websockets
import json
import time

value = 20
temp_value = 5
s_id = input("Sensor id: ")

async def send_value(s_id, value):
    async with websockets.connect(
            'ws://localhost:8000/ws/values/') as websocket:
        

        await websocket.send(json.dumps({
                    'id': s_id,
                    'type': "NO",
                    'value': value,
                }))


        await websocket.send(json.dumps({
                    'id': s_id,
                    'type': "TE",
                    'value': temp_value,
                }))


while(True):
	asyncio.get_event_loop().run_until_complete(send_value(s_id, value))
	value = value + 5
	temp_value = temp_value + 2
	
	if temp_value>=50:
		temp_value = 5

	if value>=100:
		value = 20
	
	time.sleep(1)