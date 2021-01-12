# encoding=utf-8
from paho.mqtt import client as mqtt
import Constant
import time, threading, json, zipfile, os, requests


class MqttUpgrade(object):
    # __slots__ = ('url', 'Host', 'port', 'client', 'heart_thread')

    def __init__(self):
        # {"plantformURL":"http://58.213.162.165:9012","mqttURL":"tcp://58.213.162.165:18883"}
        # xxzb.betelinfo.com
        # AEPPlay_Hi3716
        self.url = "http://xxzb.betelinfo.com:9012/rest/Terminal/v1/startService"
        self.Host = "xxzb.betelinfo.com"
        self.port = 18883
        # Constant.SN = "100177430182AD0001"
        self.heart_thread = None
        print("xxzb upgrade thread  " + Constant.SN)
        self.client = mqtt.Client(Constant.SN)
        self.connetc()

    def connetc(self):
        try:
            self.client.username_pw_set(Constant.SN, Constant.SN)
            self.client.on_connect = self.on_connect
            self.client.on_message = self.on_message
            self.client.on_log = self.on_log
            self.client.on_disconnect = self.on_disconnect
            self.client.connect(self.Host, self.port)
            # self.client.loop_forever()
            self.client.loop_start()
        except Exception as e:
            print(str(e))
            print("mqtt 连接失败，请检查网络")
            time.sleep(10)
            self.connetc()

    def on_connect(self, client, userdata, flags, rc):
        print("xxzb mqtt Connected with result code " + str(rc))
        client.subscribe(Constant.SN, 0)
        if self.heart_thread is None or not self.heart_thread.isAlive():
            self.startService()
            self.heart_thread = threading.Thread(target=self.status_thread, name='status_thread')
            self.heart_thread.start()

    def on_message(self, client, userdata, msg):
        try:
            json_str = msg.payload.decode("utf-8")
            print("收到xxzb消息" + json_str)
            json_obj = json.loads(json_str)
            if "bt0303" == json_obj.get("orderType"):
                url = json.loads(json_obj.get("orderContent")).get("url")
                self.down_and_install(url)
        except Exception as e:
            print("xxzb消息解析失败" + str(e))
        # self.queue.put({"on_message": json_str})
        # main_obj.receive_msg(json_str)

    def on_log(self, client, userdata, level, buf):
        pass
        # try:
        #     print(str(level) + str(buf))
        # except Exception as e:
        #     logging.exception(e)
        #     print(e)

    def on_disconnect(self, client, userdata, rc):
        print("mqtt断开连接")
        client.reconnect()

    """
    {
        serialNo:100177430182AD0001,
        version:1.0.0
        modelName:PA50
        cardNum:89860317240255478696
        network:1
    }
    """

    def startService(self):
        try:
            print("设备初始化接口")
            headers = {'content-type': "application/json"}
            param = {"serialNo": Constant.SN, "version": Constant.version, "modelName": "smartbox",
                     "cardNum": "",
                     "network": 1}
            res = requests.post(self.url, json=param, headers=headers,
                                verify=False, timeout=10)
            json_res = json.loads(res.text)
            print(json_res)
        except Exception as e:
            print("设备初始化失败" + str(e))

    def status_thread(self):
        try:
            pack_data = dict(serialNo=Constant.SN, devStatus="5", devSignal="2")
            pack_json = json.dumps(pack_data)
            print("xxzb 上报心跳  " + time.strftime("%Y-%m-%d %H:%M:%S"))
            self.client.publish("client_heartbeat", pack_json, 0)
        except Exception as e:
            print(str(e))
        time.sleep(60)
        self.status_thread()

    def down_and_install(self, appDownloadPath):
        print("开始下载" + appDownloadPath)
        response = requests.get(appDownloadPath)
        if response.status_code == 200:
            with open("update.zip", "wb") as f:
                f.write(response.content)
            f.close()
            print("下载完成，开始安装")
            zfile = zipfile.ZipFile("update.zip")
            zfile.extractall(path='../', members=zfile.namelist(), pwd="AEPPlay_Hi3716".encode('utf-8'))
            # zfile.extractall(path='F:\\music', members=zfile.namelist(), pwd="AEPPlay_Hi3716".encode('utf-8'))
            os.system("reboot")

# if __name__ == '__main__':
#     mqtt = MqttUpgrade()
#     mqtt.connetc()
