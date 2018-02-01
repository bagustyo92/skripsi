import paho.mqtt.client as mqtt #import the client1
from datetime import datetime
from thread import start_new_thread
import time
import sys

client = mqtt.Client("P1", clean_session=False)
broker_address = "192.168.43.30"

def on_connect(client, userdata, flags, rc):
	print "\nCONNECTING ....\n"
	time.sleep(2)
	if rc > 0 :
		print "DISCONNECTED FROM GATEWAY\n"
		time.sleep(1)
	else :
		print "CONNECTED TO GATEWAY\n"
		time.sleep(1)

def on_disconnect(client, userdata, rc):
	client.reconnect()
	print "NAH!!!!"

client.connect(broker_address)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.loop_forever()