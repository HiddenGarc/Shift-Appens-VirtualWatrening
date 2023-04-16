import random
import time

from paho.mqtt import client as mqtt_client



topic = "Temperatura"
topic1 = "Humidade"

client_id = f'python-mqtt-{random.randint(0, 1000)}'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect('broker.emqx.io', 1883)
    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        result1 = client.publish(topic1, msg)

        status = result[0]
        status1 = result1[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        
        if status1 == 0:
            print(f"Send `{msg}` to topic `{topic1}`")
        else:
            print(f"Failed to send message to topic {topic1}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
