import paho.mqtt.client as mqtt

def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))



host="mqtt.eclipse.org"
topic="sensor/temperature"
port=1883
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.connect(host,port,60)
mqttc.subscribe(topic, 0)
mqttc.loop_forever()