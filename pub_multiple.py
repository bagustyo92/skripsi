import sys
try:
    import paho.mqtt.publish as publish
except ImportError:
    import paho.mqtt.publish as publish
msgs = [{'topic':"coba/disini/pengujian", 'payload':"multiple 1"}, {'topic':"coba/disini/pengujian", 'payload':"multiple 3"},
        ("coba/disini/pengujian", "multiple 2", 0, False)]
publish.multiple(msgs, hostname="ngehubx.online")