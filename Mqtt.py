# encoding=utf-8
from paho.mqtt import client as mqtt
import logging
import Constant
import time
import threading
import json


class Mqtt():
    def __init__(self):
        # self.main_obj = main_obj
        print("设备编号：" + Constant.SN)
        self.client = mqtt.Client(Constant.SN)
        self.client_xxzb = mqtt.Client(Constant.SN)
        self.heart_thread_xxzb = None
        mqtt_thread = threading.Thread(target=self.connetc, name='mqtt_thread')
        mqtt_thread.start()
        time.sleep(10)
        mqtt_xxzb_thread = threading.Thread(target=self.connetc_for_upgrade, name='mqtt_xxzb_thread')
        mqtt_xxzb_thread.start()

    # 连接信息制播平台接收升级指令
    def connetc_for_upgrade(self):
        try:
            self.client_xxzb.username_pw_set(Constant.SN, Constant.SN)
            self.client_xxzb.on_connect = self.on_connect_xxzb
            self.client_xxzb.on_message = self.on_message
            self.client_xxzb.on_log = self.on_log
            self.client_xxzb.on_disconnect = self.on_disconnect
            self.client_xxzb.connect(Constant.MQTT_HOST_XXZB, Constant.MQTT_PORT_XXZB)
            self.client_xxzb.loop_forever()
        except Exception as e:
            print(str(e))
            print("mqtt 连接失败，请检查网络")
            time.sleep(10)
            self.connetc_for_upgrade()

    def connetc(self):
        try:
            self.client.username_pw_set(Constant.SN, Constant.PWD)
            self.client.on_connect = self.on_connect
            self.client.on_message = self.on_message
            self.client.on_log = self.on_log
            self.client.on_disconnect = self.on_disconnect
            self.client.connect(Constant.MQTT_HOST, Constant.MQTT_PORT)
            self.client.loop_forever()
        except Exception as e:
            print(str(e))
            print("mqtt 连接失败，请检查网络")
            time.sleep(10)
            self.connetc()

    def on_connect(self, client, userdata, flags, rc):
        print("------------ mqtt Connected with result code " + str(rc))
        Constant.MQTT_CLIENT = client
        Constant.time_interval = 1
        client.subscribe("device_control", 0)
        Constant.msg_queue.put({"on_connected": {"connected_code": str(rc)}})  # , "mqtt_client": client

    # 信息制播平台已连接
    def on_connect_xxzb(self, client, userdata, flags, rc):
        print("------------ xxzb mqtt Connected with result code " + str(rc))
        Constant.MQTT_CLIENT_XXZB = client
        client.subscribe(Constant.SN, 0)
        Constant.msg_queue.put({"on_connected": {"connected_code": str(rc)}})
        # if self.heart_thread_xxzb is None or not self.heart_thread_xxzb.isAlive():
        #     self.heart_thread_xxzb = threading.Thread(target=self.heart_xxzb, args=[client],
        #                                               name='heart_thread_xxzb')
        #     self.heart_thread_xxzb.start()

    # # 信息制播平台心跳
    # def heart_xxzb(self, client):
    #     try:
    #         pack_data = dict(serialNo=Constant.SN, devStatus="5", devSignal="2")
    #         pack_json = json.dumps(pack_data)
    #         print("xxzb 上报心跳  " + time.strftime("%Y-%m-%d %H:%M:%S"))
    #         self.client.publish("client_heartbeat", pack_json, 0)
    #     except Exception as e:
    #         print(str(e))
    #     time.sleep(60)
    #     self.heart_xxzb()

    def on_message(self, client, userdata, msg):
        json_str = msg.payload.decode("utf-8")
        print(json_str)
        Constant.msg_queue.put({"on_message": json_str})
        # main_obj.receive_msg(json_str)
        # t = threading.Thread(target=main_obj.receive_msg(json_str), name='receive_msg')
        # t.start()

    def on_log(self, client, userdata, level, buf):
        pass
        # try:
        #     print(str(level) + str(buf))
        # except Exception as e:
        #     logging.exception(e)
        #     print(e)

    def on_disconnect(self, client, userdata, rc):
        print("mqtt断开连接")
        Constant.time_interval=0.5
        client.reconnect()


if __name__ == '__main__':
    m = Mqtt()
    m.client_loop()
