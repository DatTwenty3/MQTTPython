import paho.mqtt.client as mqttclient
import time

def on_connect(client,userdata,flags,rc):
    print("Connected with code : " + str(rc))
    client.subscribe("BUTTON")

def on_message(client,userdata,msg):
    if(msg.payload==b'DV1On'):
        client.publish("Status", "SttDV1ON")
        print("Device 1 is ON!")
    if(msg.payload==b'DV1Off'):
        client.publish("Status", "SttDV1OFF")
        print("Device 1 is OFF!")

    if(msg.payload==b'DV2On'):
        client.publish("Status", "SttDV2ON")
        print("Device 2 is ON!")
    if(msg.payload==b'DV2Off'):
        client.publish("Status", "SttDV2OFF")
        print("Device 2 is OFF!")

broker_address="driver.cloudmqtt.com"
port=18805
user="xrsvhbaz"
password="D6CFPuh9LfjP"

client=mqttclient.Client()
client.on_connect=on_connect
client.on_message=on_message

client.connect(broker_address,port,60)
client.username_pw_set(user,password=password)

i = 0

#client.loop_forever()
client.loop_start()
time.sleep(1)
while True:
    i=i+1
    client.publish("Temp", str(i))
    client.publish("AirHumi", str(i+1))
    client.publish("SoilMois", str(i+2))
    client.publish("Power", str(i+3))
    print("Message sent!")
    time.sleep(10)
client.loop_stop()
client.disconnect()