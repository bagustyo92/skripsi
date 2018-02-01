import paho.mqtt.client as paho
import paho.mqtt.publish as publish
import sys
import time
from thread import start_new_thread

def on_publish(client, userdata, mid):
    client.disconnect()

def on_connect(client, userdata, flags, rc):
    print "\nCONNECTING ....\n"
    time.sleep(2)
    if rc == 0 :
	    print "CONNECTED TO GATEWAY\n"
	    time.sleep(2)
	    start_new_thread(send())

def on_disconnect(client, userdata, rc):
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
    client.reconnect()

client = paho.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
client.connect("192.168.43.30", 1883, 60)
#client.connect("ngehubx.online", 1883, 60)

def choice():
	pilih = raw_input("Try Again? [yes/no] : ")
	if pilih == "yes" :
		send()
	elif pilih == "no" :
		pass
	else :
		choice()

def send():
	#global status	
	msg = raw_input("Masukan Pesan yang ingin dikirim : ")
	topic = raw_input("Masukan Topik : ")
	qos = input("QoS yang ingin digunakan (0-2) : ")
	tot_msg = input("Banyaknya Pesan yang Ingin Dikirim : ")
	count = 0
	for x in range (tot_msg) :
		count = count + 1
		sent = "Msg " + str(count) + ": '" + msg + "'"
#		client.publish(topic, sent, qos)
		publish.single(topic=topic, payload=sent, qos=qos, 
						retain=False, hostname="192.168.43.62", port=1883, keepalive=60)

	print "\nPENGIRIMAN BERHASIL\n"
	time.sleep(2)
	choice()

client.loop_forever(timeout=1.0)