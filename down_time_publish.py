import paho.mqtt.client as mqtt #import the client1
from datetime import datetime
from thread import start_new_thread
import time
import sys

client = mqtt.Client("P1", clean_session=False)
broker_address = "192.168.43.30"

def check():
	if sent == rec :
		delta_time = rec_time - sent_kirim

def on_connect(client, userdata, flags, rc):
	print "\nCONNECTING ....\n"
	time.sleep(2)
	if rc == 0 :
		print "CONNECTED TO THE SERVER"
		client.subscribe("coba/down", qos=2)
	count = 0
	while rc == 0 :
		count = count + 1
		sent = str(count)
		client.publish("coba/down", sent, 2)
		print "SENDER :\n"
		print sent
		sent_time = datetime.now()
		print sent_time
		time.sleep(1)


def on_disconnect(client, userdata, rc):
	client.reconnect()
	print "DISCONNECT"

def on_message(client, userdata, message):
	print "RECEIVER :\n"
	print message
	rec_time = datetime.now()
	print rec_time

client.connect(broker_address)

client.on_connect = on_connect
client.on_disconnect = on_disconnect

client.loop_forever()