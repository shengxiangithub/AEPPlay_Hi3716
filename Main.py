# encoding=utf-8
import Hardware
from Mqtt import *
from AEP import *
import requests
from queue import Queue
from app import *
from multiprocessing import Process


class Main(object):
    # __slots__ = ('queue', 'mqtt_client', 'heart', 'aep')
    def __init__(self):
        print("当前版本：" + Constant.version)
        Constant.msg_queue = Queue(10)
        self.heart = None
        self.aep = None
        self.server = None
        self.init_terminal_conf()

    # 初始化硬件
    def init_hardware(self):
        print("初始化硬件")
        Hardware.init(self)

    def waite_write_sn_mac(self):
        Hardware.wait_sn_mac_info()
        Hardware.read_serial()
        # while True:
        #     value = input()
        #     if "serialwrite" in value:
        #         value = value.replace("serialwrite", "").replace(" ", "").replace("\"", "").replace("'", "")
        #         if value is not None:
        #             FileUtil.set_conf(Constant.SERIAL_MAC_PATH, "sn_mac", "SN", value)
        #             print("\n===SN OK !\n")
        #     elif "writemac" in value:
        #         value = value.replace("writemac", "").replace(" ", "").replace("\"", "").replace("'", "")
        #         if value is not None:
        #             FileUtil.set_conf(Constant.SERIAL_MAC_PATH, "sn_mac", "MAC", value)
        #             print("\n===MAC OK\n")
        #     elif "reboot" in value:
        #         os.system("reboot")

    # 初始化配置文件
    def init_terminal_conf(self):
        if not FileUtil.exists(Constant.SERIAL_MAC_PATH):
            print("未找到sn配置文件")
            self.waite_write_sn_mac()
        else:
            try:
                sn = FileUtil.get_conf(Constant.SERIAL_MAC_PATH, "sn_mac", "SN")
                if sn is None:
                    print("有配置文件但是没有SN值")
                    self.waite_write_sn_mac()
                else:
                    Constant.SN = sn
                mac = FileUtil.get_conf(Constant.SERIAL_MAC_PATH, "sn_mac", "MAC")
                if mac is None:
                    print("有配置文件但是没有MAC值")
                    self.waite_write_sn_mac()
                else:
                    Constant.MAC = mac
            except Exception as e:
                print("配置文件异常" + str(e))
                self.waite_write_sn_mac()
        if FileUtil.exists(Constant.CONF_FILE_PATH):
            conf_json = FileUtil.read_json_data(Constant.CONF_FILE_PATH)
            # print(conf_json)
            mqttep = conf_json.get("mqttep")
            if "//" in mqttep and ":" in mqttep:
                Constant.IP = conf_json.get("ip")
                Constant.IPMASK = conf_json.get("ipmask")
                Constant.GATEWAY = conf_json.get("gateway")
                Constant.DNS1 = conf_json.get("dns1")
                Constant.DNS2 = conf_json.get("dns2")
                print(str(Constant.IP) + "  " + str(Constant.IPMASK) + "  " + str(Constant.GATEWAY) + " " + str(
                    Constant.DNS1) + "  " + str(Constant.DNS2))
                Constant.G4EN = conf_json.get("g4en")
                Constant.MQTT_HOST = mqttep.split("//")[1].split(":")[0]
                Constant.MQTT_PORT = int(mqttep.split("//")[1].split(":")[1])
                Constant.PWD = conf_json.get("mqttpass")
                Constant.DES_KEY = conf_json.get("despass")
                Constant.USELESS_SN = Constant.SN
                Constant.SN = conf_json.get("productid") + Constant.SN[-6:]
                # Constant.USELESS_SN = conf_json.get("sn")
                print(str(Constant.MQTT_HOST) + " " + str(Constant.MQTT_PORT) + " " + " " + str(Constant.SN))
                self.init_hardware()
                wating_queue_msg = threading.Thread(target=self.wating_queue_msg_thread,
                                                    name='wating_queue_msg_thread')
                wating_queue_msg.start()
                Mqtt()
                self.start_service()
        else:
            Hardware.wait_conf_info()
            print("未发现配置文件，请先配置平台信息")
            cmd = "ifconfig lo up & ifconfig eth0 " + str(Constant.IP) + " netmask " + str(Constant.IPMASK)
            print(cmd)
            os.system(cmd)
            self.start_server_thread()
        # app.debug = False
        # app.run(host=Constant.IP, port=80)
        # server = Process(app.run(host=Constant.IP, port=80))

    def stop_server(self):
        try:
            print('>>>>>>>>> stop server <<<<<<<<<<<<')
            self.server.terminate()
            self.server.join()
        except Exception as e:
            print("stpo server failed" + str(e))

    def start_server_thread(self):
        self.server = Process(target=self.start_server)
        self.server.start()

    def start_server(self):
        try:
            print(">>>>>>>>>>> start server <<<<<<<<<<<<<<")
            app.run(host=Constant.IP, port=80)
            # TODO
            # app.run(host="localhost", port=80)
        except Exception as e:
            print("start server failed" + str(e))

    def start_service(self):
        try:
            print("设备调用初始化接口")
            headers = {'content-type': "application/json"}
            param = {"serialNo": Constant.SN, "version": Constant.version, "modelName": "EB-TE-PA50-05",
                     "cardNum": "",
                     "network": Constant.network}
            res = requests.post(Constant.START_SERVICE_URL + "/rest/Terminal/v1/startService", json=param,
                                headers=headers, verify=False, timeout=10)
            json_res = json.loads(res.text, encoding='utf-8')
            if json_res is not None and "00000000" == json_res.get("code") and json_res.get("payload") is not None:
                service_time = json_res.get("payload").get("serviceTime")
                if "-" in service_time and " " in service_time and ":" in service_time:
                    print("更新设备时间:" + service_time)
                    os.system("date -s '" + service_time + "'")
            print(json_res)
        except Exception as e:
            print("设备初始化失败" + str(e))

    def wating_queue_msg_thread(self):
        print("wating_queue_msg start ...")
        try:
            while True:
                queue_msg = Constant.msg_queue.get()
                if queue_msg is not None:
                    print(str(queue_msg))
                    key = list(queue_msg.keys())[0]
                    if key == "on_connected":  # MQTT已连接
                        connected_data = queue_msg["on_connected"]
                        # print("mqtt connected with code :" + connected_data.get("connected_code"))
                        if connected_data is not None and connected_data.get("connected_code") == "0":
                            if self.aep is None:
                                print("开启AEP业务....")
                                self.aep = AEP()
                    elif key == "on_message":  # 收到MQTT消息
                        if self.aep is not None:
                            self.aep.on_message(queue_msg["on_message"])
                        else:
                            print("self.aep is None can not deal message")
                    elif key == "play_next":  # 播放下一首
                        self.aep.play_next()
                    elif key == "aep_heart":
                        # print(">>>>>>>>>>>>>>>>>>>>>>>>>> aep_heart")
                        time.sleep(0.3)
                        if "volume_on" == queue_msg["aep_heart"]:
                            Hardware.switch_voice(True)
                        else:
                            Hardware.switch_voice(False)
                        if self.aep is not None:
                            self.aep.change_heart()
        except Exception as e:
            print("wating_queue_msg Exception：" + str(e))
            self.wating_queue_msg_thread()


if __name__ == '__main__':
    main = Main()
