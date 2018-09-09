# chat/consumers.py
from channels.generic.websocket import WebsocketConsumer
from dashboard.models import Sensor, ValuesReceived
import json

class ValueConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):

        sensors = Sensor.objects.all()

        for sensor in sensors:
            try:
                last_noise = ValuesReceived.objects.filter(sensor = Sensor.objects.get(name=sensor.name), value_type=ValuesReceived.NOISE).order_by('-timestamp')[0]
            except Exception as e:
                last_noise = []

            try:
                last_temperature = ValuesReceived.objects.filter(sensor = Sensor.objects.get(name=sensor.name), value_type=ValuesReceived.TEMPERATURE).order_by('-timestamp')[0]
            except Exception as e:
                last_temperature = []

            if last_noise != []:
                self.send(text_data=json.dumps({
                    'id': sensor.name,
                    'type': ValuesReceived.NOISE,
                    'value': last_noise.value,
                    'timestamp': [last_noise.timestamp.year, last_noise.timestamp.month, last_noise.timestamp.day, last_noise.timestamp.hour, last_noise.timestamp.minute, last_noise.timestamp.second]
                }))

            if last_temperature != []:
                self.send(text_data=json.dumps({
                    'id': sensor.name,
                    'type': ValuesReceived.TEMPERATURE,
                    'value': last_temperature.value,
                    'timestamp': [last_temperature.timestamp.year, last_temperature.timestamp.month, last_temperature.timestamp.day, last_temperature.timestamp.hour, last_temperature.timestamp.minute, last_temperature.timestamp.second]
                }))


class ValueReceiver(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):

        text_data_json = json.loads(text_data)
        
        sensor_id = text_data_json['id']
        message_type = text_data_json['type']
        message_value = text_data_json['value']

        try:
            sensor = Sensor.objects.get(name=sensor_id)
        except Exception as e:
            print(sensor_id+"Not found!")
            return

        new_value = ValuesReceived.objects.create(value = message_value, sensor = sensor, value_type = message_type)
        new_value.save()

