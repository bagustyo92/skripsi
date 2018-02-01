import paho.mqtt.client as mqtt #import the client1
from datetime import datetime
from thread import start_new_thread
from random import randint
import time
import sys

# client = mosquitto.Mosquitto(clientid, userdata=userdata, clean_session=False)
client = mqtt.Client(clean_session=True)

heartbeat_file_path = "heartbeat.txt"
date_time_display_format = '%A, %B %d, %Y at %I:%M %p'
system_down_time = ""
broker_address = "192.168.43.30"

def count_time():
	if time_disconnect != 0 :
		delta_time = time_disconnect - time_connect
		print("Your Gateway Has been disconnect ", delta_time, " second")
	else :
		print "\nYOUR GATEWAY NOT DISCONNECT"

def send():
	msg = raw_input("Pesanye ape : ")
	qos = input("QoS berape : ")
	choice = input("Berapa kali : ")
	print "\nPublishing message to topic : (coba/disini/pengujian)"
	time.sleep(2)
	print("Subscribing to topic : (coba/disini/pengujian)")
	client.subscribe("coba/disini/pengujian", qos=2)
	count = 0
	for i in range (choice) :
		count = count + 1
		sent = str(count) + " " + msg
		client.publish("coba/disini/pengujian", sent, qos)
	print "FINISH SENDING MESSAGE\n"
	count_time()
	time.sleep(2)
	# send()

time_connect = 0
time_disconnect = 0

def on_connect(client, userdata, flags, rc):
    # global time_status
    # time_status = True
    global time_connect
    time_connect = time.time()
    print "\nCONNECTING ....\n"
    time.sleep(2)
    if rc == 0 :
	    print "CONNECTED TO GATEWAY\n"
	    time.sleep(2)
	    send()
	    # write_delta_time()

def on_disconnect(client, userdata, rc):
    # if time_status == False :
    global time_disconnect
    time_disconnect = time.time()
    
    if rc == 1 :
    	print "CONNECTION REFUSED : incorrect protocol version!"
    elif rc == 2 :
    	print "CONNECTION REFUSED : invalid client identifier!"
    elif rc == 3 :
    	print "CONNECTION REFUSED : server unavailable!"
    elif rc == 4 :
    	print "CONNECTION REFUSED : bad username or password!"
    elif rc == 5 :
    	print "CONNECTION REFUSED : not authorised!"
    else :
    	print "Currently unused"
    time.sleep(2)
    # while rc > 0 :
    # 	start_new_thread(heartbeat_start())
    client.reconnect()
    # client.reconnect_delay_set(min_delay=1, max_delay=120)

def on_message(client, userdata, message):
	print("message received ", str(message.payload.decode("utf-8")))
	print("message topic=",message.topic)
	print("message qos=",message.qos)
	print("message retain flag=",message.retain)

client.on_message = on_message #attach function to callback
client.connect(broker_address)
client.on_connect = on_connect
client.on_disconnect = on_disconnect #connect to broker

client.loop_start()
time.sleep(900)
print("\nTIME OUT!\nDISCONNECTED FROM SERVER")
client.loop_stop()#stop the loop