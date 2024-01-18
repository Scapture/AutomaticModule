import paho.mqtt.client as mqtt

def run(pid):
    # 변경
    broker_ip = "192.168.0.15" # 현재 이 컴퓨터를 브로커로 설정
    topic = pid
    client = mqtt.Client()
    client.connect(broker_ip, 1883, 60)
    client.publish(topic, "end", qos=0)
    client.disconnect()


