import json
import paho.mqtt.client as mqtt
from time import sleep
import httpclient as http
import asyncore
import time
#import unicornhat as uh

gv_ipaddress = "172.20.10.10"
gv_username = "admin"
gv_password = "1111"

ch = "steve.io/myNVR"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(ch)

def send_command(username, password, host, url):
    c = http.HttpClient(username, password, host, url)

    
def on_message(client, userdata, msg):
    print(msg.payload)
    if(msg.payload[:1]=="{"):
        payload = json.loads(msg.payload)

    	if("intensity" in payload):
    		brightness = float(payload["intensity"] * 0.01)
    		print(str(brightness))

    	elif("channel" in payload):
            print("channel")
            print(payload["channel"])
            ch = str(hex(payload["channel"]))
            ch = ch[ 2 : len(ch) ]
            print ch
            myurl = "/serial?port=1&write=730020000" + ch + "0000"
            send_command(gv_username, gv_password, gv_ipaddress, myurl)

    	elif("playback" in payload):
            print("playback")
            send_command(gv_username, gv_password, gv_ipaddress, "/serial?port=1&write=73000800000000")
            time.sleep(1)
            send_command(gv_username, gv_password, gv_ipaddress, "/serial?port=1&write=73000300000000") # Enter
            time.sleep(1)
            send_command(gv_username, gv_password, gv_ipaddress, "/serial?port=1&write=73000800000000")
            time.sleep(1)
            send_command(gv_username, gv_password, gv_ipaddress, "/serial?port=1&write=73000300000000") # Enter
        elif("sixteen" in payload):
            print("sixteen")
            send_command(gv_username, gv_password, gv_ipaddress, "/serial?port=1&write=73002100100000")  # display 16

        elif("quad" in payload):
            print("quad")
            send_command(gv_username, gv_password, gv_ipaddress, "/serial?port=1&write=73002100040000")  # display quid

        elif("fastforward" in payload):
            print("fastforward")
            send_command(gv_username, gv_password, gv_ipaddress, "/serial?port=1&write=73000500000000")  # fast forward

        elif("fastrewind" in payload):
            print("fastrewind")
            send_command(gv_username, gv_password, gv_ipaddress, "/serial?port=1&write=73000400000000")  # fast rewind

        elif("playstop" in payload):
            print("Stop playing")
            send_command(gv_username, gv_password, gv_ipaddress, "/serial?port=1&write=73000A00000000")  # stop
            time.sleep(1)
            send_command(gv_username, gv_password, gv_ipaddress, "/serial?port=1&write=73000200000000")  # ESC
            time.sleep(1)
            send_command(gv_username, gv_password, gv_ipaddress, "/serial?port=1&write=73000A00000000")  # stop
            time.sleep(1)
            send_command(gv_username, gv_password, gv_ipaddress, "/serial?port=1&write=73000200000000")  # ESC
            time.sleep(1)
            send_command(gv_username, gv_password, gv_ipaddress, "/serial?port=1&write=73002100100000")  # 16 view

        elif("quad" in payload):
            print("quad")
            send_command(gv_username, gv_password, gv_ipaddress, "/serial?port=1&write=73002100040000")  # display quad

send_command(gv_username, gv_password, gv_ipaddress, "/serial?port=1&write=73002100100000")           
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.cc", 1883, 60)
client.loop_forever()
