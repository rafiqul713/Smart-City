import paho.mqtt.publish as publish

host = "mqtt.eclipse.org"
port = 1883
topic = "sensor/temperature"
payload = "16 degree celsius"

while True:
	publish.single(topic,payload,hostname=host)