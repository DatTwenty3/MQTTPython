import paho.mqtt.client as mqttclient
import time
#LoRa
import serial
from time import sleep
ser = serial.Serial('/dev/ttyAMA0',9600)


def on_connect(client,userdata,flags,rc):
    print("Connected with code : " + str(rc))
    client.subscribe("BUTTON")

def on_message(client,userdata,msg):
    if(msg.payload==b'DV1On'):
        #LoRa data send
        ser.write((" DV1On"+"\r").encode())
    if(msg.payload==b'DV1Off'):
        #LoRa data send
        ser.write((" DV1Off"+"\r").encode())

    if(msg.payload==b'DV2On'):
        #LoRa data send
        ser.write((" DV2On"+"\r").encode())
    if(msg.payload==b'DV2Off'):
        #LoRa data send
        ser.write((" DV2Off"+"\r").encode())

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
    #LoRa
    if (ser.in_waiting>0):
        dataFromArduino = ser.read(ser.inWaiting())
        if (dataFromArduino==b'SttDV1ON'):
            #MQTT publish
            client.publish("Status", "SttDV1ON")
            print("Device 1 is ON!")
        elif (dataFromArduino==b'SttDV1OFF'):
            #MQTT publish
            client.publish("Status", "SttDV1OFF")
            print("Device 1 is OFF!")
            
        elif (dataFromArduino==b'SttDV2ON'):
            #MQTT publish
            client.publish("Status", "SttDV2ON")
            print("Device 2 is ON!")
        elif (dataFromArduino==b'SttDV2OFF'):
            client.publish("Status", "SttDV2OFF")
            #MQTT publish
            client.publish("Status", "SttDV2OFF")
            print("Device 2 is OFF!")
        elif (str(dataFromArduino).find("Temp") > 0):
            temp = str(dataFromArduino)
            temp = temp.replace(" Temp","")
            temp = temp.replace("b","")
            temp = temp.replace("'","")
            print("Temperature: ")
            print(int(temp))
            client.publish("Temp", int(temp))
        elif (str(dataFromArduino).find("Humi") > 0):
            airHumi = str(dataFromArduino)
            airHumi = airHumi.replace(" Humi","")
            airHumi = airHumi.replace("b","")
            airHumi = airHumi.replace("'","")
            print("Humidity: ")
            print(int(airHumi))
            client.publish("AirHumi", int(airHumi))
        elif (str(dataFromArduino).find("SoilMois") > 0):
            soilMois = str(dataFromArduino)
            soilMois = soilMois.replace(" SoilMois","")
            soilMois = soilMois.replace("b","")
            soilMois = soilMois.replace("'","")
            print("Soil Moisture: ")
            print(int(soilMois))
            client.publish("SoilMois", int(soilMois))
        elif (str(dataFromArduino).find("ORP") > 0):
            ORP = str(dataFromArduino)
            ORP = ORP.replace(" ORP","")
            ORP = ORP.replace("b","")
            ORP = ORP.replace("'","")
            print("ORP: ")
            print(int(ORP))
            client.publish("ORP", int(ORP))
        elif (str(dataFromArduino).find("pH") > 0):
            pH = str(dataFromArduino)
            pH = pH.replace(" pH","")
            pH = pH.replace("b","")
            pH = pH.replace("'","")
            print("pH: ")
            print(int(pH))
            client.publish("pH", int(pH))
        
        
        #else:
            #dataFromSensor = dataFromArduino
            #print(dataFromSensor)
            #AirHumi = dataFromSensor//1000000
            #Temp = (dataFromSensor%100000)//1000
            #SoilMois = (dataFromSensor%100000)%1000
            #client.publish("AirHumi", AirHumi)
            #client.publish("Temp", Temp)
            #client.publish("SoilMois", SoilMois)
            
    
    #MQTT
    #i=i+1
    #client.publish("Temp", str(i))
    #client.publish("AirHumi", str(i+1))
    #client.publish("SoilMois", str(i+2))
    #client.publish("Power", str(i+3))
    #print("Message sent!")
    time.sleep(0.5)
    
client.loop_stop()
client.disconnect()