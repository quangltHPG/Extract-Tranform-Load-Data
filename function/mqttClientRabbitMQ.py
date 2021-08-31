import datetime
import json
import paho.mqtt.client
#import sense_hat
import time
sleepTime = 1
# MQTT details
mqttDeviceId = "Raspberry-Pi:Prototype"
mqttBrokerHost = "192.168.113.32"
mqttBrokerPort = 1883
mqttUser = "<quanglt>"
mqttPassword = "<hoilamgi1>"
mqttTelemetryTopic = "RPi.Data"
#sense = sense_hat.SenseHat()
# Callback methods
def on_connect(client, userdata, flags, rc):
    if rc == 0:
          print("Connected to MQTT broker (RC: %s)" % rc)
    else:
          print("Connection to MQTT broker failed (RC: %s)" % rc)
def on_log(client, userdata, level, buf):
    print(buf)
def on_publish(client, userdata, mid):
    print("Data published (Mid: %s)" % mid)
def on_disconnect(client, userdata, rc):
    if rc != 0:
          print("Unexpected disconnect")
    print("Disconnected from MQTT broker")
mqttClient = paho.mqtt.client.Client()
mqttClient.username_pw_set(mqttUser, mqttPassword)
# Register callbacks
mqttClient.on_connect = on_connect
mqttClient.on_log = on_log
mqttClient.on_publish = on_publish
mqttClient.on_disconnnect = on_disconnect
# Connect to MQTT broker
mqttClient.connect(mqttBrokerHost, mqttBrokerPort, 60)
mqttClient.loop_start()
# Collect telemetry information from Sense HAT and publish to MQTT broker in JSON format
while True:
    telemetryData = {}
    telemetryData["DeviceId"] = mqttDeviceId
    telemetryData["Timestamp"] = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
#    telemetryData["Temperature"] = str(round(sense.get_temperature(), 2))
#    telemetryData["Humidity"] = str(round(sense.get_humidity(), 2))
#    telemetryData["Pressure"] = str(round(sense.get_pressure(), 2))
    telemetryDataJson = json.dumps(telemetryData)
    mqttClient.publish(mqttTelemetryTopic, telemetryDataJson, 1)
    time.sleep(sleepTime)
mqttClient.loop_stop()
mqttClient.disconnect()
