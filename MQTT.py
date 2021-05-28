import paho.mqtt.client as mqttclient
import time
#GUI
from tkinter import *
import threading
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

#GUI
win = Tk()
win.title('LEDAT RASPBERRY GATEWAY')
win.configure(bg = 'black')
#Name
labelName = Label(win,
                  text = "LEDAT RASPBERRY GATEWAY",
                  bg = 'white',
                  fg = 'black',
                  font = 'Oswald 25 bold',
                  relief = "groove",
                  borderwidth = 5)
labelName.grid(row = 0, column = 2)
#Status Relay
labelSensor = Label(win,
                    text = "SENSOR",
                    bg = 'black',
                    fg = '#00BCD4',
                    font = 'Oswald 25 bold')
labelSensor.grid(row = 1, column = 0, sticky = W)
#Temperature
labelTemp = Label(win,
                text = "TEMPERATURE: ",
                bg = 'black',
                fg = 'white',
                font = 'Oswald 25 bold')
labelTemp.grid(row = 2, column = 0, sticky = W)
labelTempVal = Label(win,
                   text = "null",
                   bg = 'black',
                   fg = '#FFEB3B',
                   font = 'Oswald 25 bold')
labelTempVal.grid(row = 2, column = 1, sticky = E)
labelTempUnit = Label(win,
                   text = " °C",
                   bg = 'black',
                   fg = '#FFEB3B',
                   font = 'Oswald 25 bold')
labelTempUnit.grid(row = 2, column = 2, sticky = W)
#Air Humi
labelAirHumi = Label(win,
                text = "AIR HUMIDITY: ",
                bg = 'black',
                fg = 'white',
                font = 'Oswald 25 bold')
labelAirHumi.grid(row = 3, column = 0, sticky = W)
labelAirHumiVal = Label(win,
                   text = "null",
                   bg = 'black',
                   fg = '#FFEB3B',
                   font = 'Oswald 25 bold')
labelAirHumiVal.grid(row = 3, column = 1, sticky = E)
labelAirHumiUnit = Label(win,
                   text = " %",
                   bg = 'black',
                   fg = '#FFEB3B',
                   font = 'Oswald 25 bold')
labelAirHumiUnit.grid(row = 3, column = 2, sticky = W)
#SoilMois
labelSoilMois = Label(win,
                text = "SOIL MOISTURE: ",
                bg = 'black',
                fg = 'white',
                font = 'Oswald 25 bold')
labelSoilMois.grid(row = 4, column = 0, sticky = W)
labelSoilMoisVal = Label(win,
                   text = "null",
                   bg = 'black',
                   fg = '#FFEB3B',
                   font = 'Oswald 25 bold')
labelSoilMoisVal.grid(row = 4, column = 1, sticky = E)
labelSoilMoisUnit = Label(win,
                   text = " %",
                   bg = 'black',
                   fg = '#FFEB3B',
                   font = 'Oswald 25 bold')
labelSoilMoisUnit.grid(row = 4, column = 2, sticky = W)
#pH
labelPH = Label(win,
                text = "WATER pH: ",
                bg = 'black',
                fg = 'white',
                font = 'Oswald 25 bold')
labelPH.grid(row = 5, column = 0, sticky = W)
labelPHVal = Label(win,
                   text = "null",
                   bg = 'black',
                   fg = '#FFEB3B',
                   font = 'Oswald 25 bold')
labelPHVal.grid(row = 5, column = 1, sticky = E)
#ORP
labelORP = Label(win,
                 text = "WATER ORP: ",
                 bg = 'black',
                 fg = 'white',
                 font = 'Oswald 25 bold')
labelORP.grid(row = 6, column = 0, sticky = W)
labelORPVal = Label(win,
                    text = "null",
                    bg = 'black',
                    fg = '#FFEB3B',
                    font = 'Oswald 25 bold')
labelORPVal.grid(row = 6, column = 1, sticky = E)
#Turbidity
labelTurbi = Label(win,
                 text = "TURBIDITY: ",
                 bg = 'black',
                 fg = 'white',
                 font = 'Oswald 25 bold')
labelTurbi.grid(row = 7, column = 0, sticky = W)
labelTurbiVal = Label(win,
                    text = "null",
                    bg = 'black',
                    fg = '#FFEB3B',
                    font = 'Oswald 25 bold')
labelTurbiVal.grid(row = 7, column = 1, sticky = E)
labelTurbiUnit = Label(win,
                   text = " V",
                   bg = 'black',
                   fg = '#FFEB3B',
                   font = 'Oswald 25 bold')
labelTurbiUnit.grid(row = 7, column = 2, sticky = W)
#Status Relay
labelStatus = Label(win,
                    text = "STATUS DEVICE",
                    bg = 'black',
                    fg = '#00BCD4',
                    font = 'Oswald 25 bold',)
labelStatus.grid(row = 8, column = 0, sticky = W)
#Light
labelLight = Label(win,
                 text = "LIGHT: ",
                 bg = 'black',
                 fg = 'white',
                 font = 'Oswald 25 bold')
labelLight.grid(row = 9, column = 0, sticky = W)
labelLightStt = Label(win,
                    text = "",
                    bg = 'black',
                    fg = '#FFEB3B',
                    font = 'Oswald 25 bold')
labelLightStt.grid(row = 9, column = 1, sticky = E)
#Water Pump
labelWaPump = Label(win,
                 text = "WATER PUMP: ",
                 bg = 'black',
                 fg = 'white',
                 font = 'Oswald 25 bold')
labelWaPump.grid(row = 10, column = 0, sticky = W)
labelWaPumpStt = Label(win,
                    text = "",
                    bg = 'black',
                    fg = '#FFEB3B',
                    font = 'Oswald 25 bold')
labelWaPumpStt.grid(row = 10, column = 1, sticky = E)

#client.loop_forever()
client.loop_start()                  
time.sleep(1)
def UpdatePara():
    while True:
        #LoRa
        if (ser.in_waiting>0):
            dataFromArduino = ser.read(ser.inWaiting())
            if (dataFromArduino==b'SttDV1ON'):
                #MQTT publish
                client.publish("Status", "SttDV1ON")
                print("Device 1 is ON!")
                labelLightStt.config(text = "ON", fg = 'green')
            elif (dataFromArduino==b'SttDV1OFF'):
                #MQTT publish
                client.publish("Status", "SttDV1OFF")
                print("Device 1 is OFF!")
                labelLightStt.config(text = "OFF", fg = 'red')
            
            elif (dataFromArduino==b'SttDV2ON'):
                #MQTT publish
                client.publish("Status", "SttDV2ON")
                print("Device 2 is ON!")
                labelWaPumpStt.config(text = "ON", fg = 'green')
            elif (dataFromArduino==b'SttDV2OFF'):
                client.publish("Status", "SttDV2OFF")
                #MQTT publish
                client.publish("Status", "SttDV2OFF")
                print("Device 2 is OFF!")
                labelWaPumpStt.config(text = "OFF", fg = 'red')
            elif (str(dataFromArduino).find("Temp") > 0):
                temp = str(dataFromArduino)
                temp = temp.replace(" Temp","")
                temp = temp.replace("b","")
                temp = temp.replace("'","")
                print("Temperature: ")
                print(int(temp))
                client.publish("Temp", int(temp))
                labelTempVal.config(text = temp)
            elif (str(dataFromArduino).find("Humi") > 0):
                airHumi = str(dataFromArduino)
                airHumi = airHumi.replace(" Humi","")
                airHumi = airHumi.replace("b","")
                airHumi = airHumi.replace("'","")
                print("Humidity: ")
                print(int(airHumi))
                client.publish("AirHumi", int(airHumi))
                labelAirHumiVal.config(text = airHumi)
            elif (str(dataFromArduino).find("SoilMois") > 0):
                soilMois = str(dataFromArduino)
                soilMois = soilMois.replace(" SoilMois","")
                soilMois = soilMois.replace("b","")
                soilMois = soilMois.replace("'","")
                print("Soil Moisture: ")
                print(int(soilMois))
                client.publish("SoilMois", int(soilMois))
                labelSoilMoisVal.config(text = soilMois)
            elif (str(dataFromArduino).find("ORP") > 0):
                ORP = str(dataFromArduino)
                ORP = ORP.replace(" ORP","")
                ORP = ORP.replace("b","")
                ORP = ORP.replace("'","")
                print("ORP: ")
                print(int(ORP))
                client.publish("ORP", int(ORP))
                labelORPVal.config(text = ORP)
            elif (str(dataFromArduino).find("pH") > 0):
                pH = str(dataFromArduino)
                pH = pH.replace(" pH","")
                pH = pH.replace("b","")
                pH = pH.replace("'","")
                print("pH: ")
                print(float(pH))
                client.publish("pH", float(pH))
                labelPHVal.config(text = pH)
            elif (str(dataFromArduino).find("DS") > 0):
                DS = str(dataFromArduino)
                DS = DS.replace(" DS","")
                DS = DS.replace("b","")
                DS = DS.replace("'","")
                print("Water Temperature: ")
                print(int(DS))
                client.publish("WaTemp", int(DS))
            elif (str(dataFromArduino).find("Turbi") > 0):
                Turbi = str(dataFromArduino)
                Turbi = Turbi.replace(" Turbi","")
                Turbi = Turbi.replace("b","")
                Turbi = Turbi.replace("'","")
                print("Turbidity: ")
                print(float(Turbi))
                client.publish("Turbi", float(Turbi))
                labelTurbiVal.config(text = Turbi)
        
        time.sleep(0.5)

setTextThr = threading.Thread(target = UpdatePara)
setTextThr.start()
win.mainloop()
client.loop_stop()
client.disconnect()