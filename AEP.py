# encoding=utf-8

import requests, zipfile, json, DESUtils, os, Hardware
from Player import *


class AEP(object):
    # __slots__ = ('mqtt_client','heart', 'player')

    def __init__(self):
        self.player = Player()
        self.heart = threading.Thread(target=self.update_heart, name="heart_thread")
        self.heart.start()
        update_some_info_thread = threading.Thread(target=self.update_some_info,
                                                   name="update_some_info_thread")
        update_some_info_thread.start()
        self.query_task()

    def play_next(self):
        self.player.choise_one_to_play()

    """
    {
    "action": "update",
    "device_id": "设备id",
    "status": 1,
    "task_number": "广播消息编码",
    "volume": 1,
    "rssi": 1,
    }
    """

    # 心跳改变立刻上报
    def change_heart(self):
        try:
            print("上报心跳： " + time.strftime("%Y-%m-%d %H:%M:%S"))
            pack_data = dict(action="update", device_id=Constant.SN, status=Constant.STATUS,
                             task_number=Constant.TASK_NUM, volume=Constant.VOLUME,
                             rssi=Constant.rssi)
            self.update_pack_data(pack_data)
        except Exception as e:
            print(str(e))

    """{ 
        "action": "info_report", 
        "device_id": "设备id", 
        "firmware_version": "ct2.1", 
        "hardware_version": "v1.2", 
        "iccid": "iccid编号", 
    } """

    # 上报iccid和无线参数
    def update_some_info(self):
        try:
            while Constant.MQTT_CLIENT is None or not Constant.MQTT_CLIENT.is_connected():
                time.sleep(10)
            Hardware.get_iccid()
            if "1" == Constant.G4EN and "" == Constant.iccid:
                time.sleep(60)
                Hardware.get_iccid()
                if "" == Constant.iccid:
                    time.sleep(60)
                    Hardware.get_iccid()
            print("上报iccid： " + time.strftime("%Y-%m-%d %H:%M:%S"))
            pack_data = dict(action="info_report", device_id=Constant.SN, firmware_version="ct2.1",
                             hardware_version="v1.2", iccid=Constant.iccid)
            self.update_pack_data(pack_data)
        except Exception as e:
            print(str(e))

        if "1" != Constant.G4EN:
            print("非4G设备不上报基站信息")
            return
        """{ 
                "action": " signal_report", 
                "device_id": "设备id", 
                "rsrp": rsrp值, 
                "pci": pci值, 
                "ecl": ecl值, 
                "cell_id": cell_id值, 
                }"""
        try:
            Hardware.get_rsrp_pci_cellid_rssi()
            while "" == Constant.rsrp or "" == Constant.pci or "" == Constant.cell_id:
                time.sleep(60)
                Hardware.get_rsrp_pci_cellid_rssi()
            print("上报基站信息： " + time.strftime("%Y-%m-%d %H:%M:%S"))
            pack_data = dict(action="signal_report", device_id=Constant.SN, rsrp=Constant.rsrp,
                             pci=Constant.pci, ecl=Constant.ecl, cell_id=Constant.cell_id)
            self.update_pack_data(pack_data)
        except Exception as e:
            print(str(e))

    # 上报心跳
    def update_heart(self):
        while True:
            self.change_heart()
            self.heart_xxzb()
            time.sleep(40)
        # self.update_heart()  # TODO递归次数不能太多

    # 信息制播平台心跳
    def heart_xxzb(self):
        try:
            pack_data = dict(serialNo=Constant.SN, devStatus="5", devSignal="2")
            pack_json = json.dumps(pack_data)
            print("xxzb 上报心跳  " + time.strftime("%Y-%m-%d %H:%M:%S"))
            if Constant.MQTT_CLIENT_XXZB is not None and Constant.MQTT_CLIENT_XXZB.is_connected():
                Constant.MQTT_CLIENT_XXZB.publish("client_heartbeat", pack_json, 0)
            else:
                print("error xxzb 心跳失败，mqtt 未连接")
        except Exception as e:
            print(str(e))

    """{
       "action": "query_task",
       "device_id": "设备id",	
       }
       """

    # 查询任务
    def query_task(self):
        try:
            while Constant.MQTT_CLIENT is None or not Constant.MQTT_CLIENT.is_connected():
                time.sleep(10)
            time.sleep(1)
            print("查询待播任务...")
            pack_data = dict(action="query_task", device_id=Constant.SN)
            self.update_pack_data(pack_data)
        except Exception as e:
            print("查询任务失败：" + str(e))

    """{
    "action": "query_task"	,
    “task”:[ 开播指令按时间降序排序]
    }
    """

    # 查询任务返回
    def query_task_back(self, rtsp_data_json):
        if rtsp_data_json.get("task") is not None:
            tasks = json.loads(rtsp_data_json.get("task"))
            if tasks is not None and len(tasks) > 0:
                self.player.add_tasks([rtsp_data_json])

    """{
    "action": "play",
    "task_number": "广播消息编码",
    "streaming_url": "rtsp://ip:port/path",
    "text": "文本内容",
    "level": 3,
    "volume": 8
    }
    """

    # 播放
    def play(self, rtsp_data_json):
        self.player.add_tasks([rtsp_data_json])

    """{
    "action": "control",
    "volume":9,
    "run":true,
    }
    """

    # 控制音量
    def control_volume(self, rtsp_data_json):
        pass

    """{
    "action": "play_stop",
    "task_number": "广播消息编码",
    }
    """

    # 停止播放
    def stop(self, rtsp_data_json):
        task_number = rtsp_data_json.get("task_number")
        if task_number is not None and len(task_number) > 0:
            self.player.cancle_task(task_number)
        else:
            print("停播任务失败，task_number不合法")

    """{
    "action": "upgrade",
    "version_code":3,//新版本号
    "md5":"6c7b7cd1007f3324badb4637632fd3ed",
    "download_url":"http://47.96.132.39:15010/OTA_IMG_TS.bin",
    }
    """
    """
    {
    "orderType":"bt0303",
    "orderContent":"{"appId":"android_serialport_api.sample","name":"1.0.1","url":"http://58.213.162.165:12224/upload/2KRdSd6ae5614d252SbNRNdJ5K5JSed1/other/c377d1dc5e3811eabdf1000c292b5231_T_Hi3716_V1.0.2.bin"}",
    "orderId":"1235247776884056065"
    }
    """

    def down_and_install(self, appDownloadPath):
        print("开始下载" + appDownloadPath)
        response = requests.get(appDownloadPath)
        if response.status_code == 200:
            with open("update.zip", "wb") as f:
                f.write(response.content)
            f.close()
            print("下载完成，开始安装")
            zfile = zipfile.ZipFile("update.zip")
            try:
                zfile.extractall(path='./', members=zfile.namelist(), pwd="AEPPlay_Hi3716".encode('utf-8'))
            # zfile.extractall(path='F:\\music', members=zfile.namelist(), pwd="AEPPlay_Hi3716".encode('utf-8'))
            except Exception as e:
                print("升级失败" + str(e))
                path = zfile.namelist()[0].split("/")[0]
                os.system("rm -r " + path)
                print("删除升级包")
            os.system("reboot")

    # 设备升级
    def upgrade(self, order_content):
        print(">>>>>>>>>>>>>>>>>>>>>>>升级中...")
        content = json.loads(order_content, encoding="utf-8")
        if content is not None:
            url = content.get("url")
            if url is not None:
                self.down_and_install(url)

    def update_pack_data(self, pack_data):
        pack_json = json.dumps(pack_data)
        print(pack_json)
        data = DESUtils.encrypt(pack_json)
        heart_data = dict(type=2, data=data)
        heart_data_json = json.dumps(heart_data)
        # print(heart_data_json)
        if Constant.MQTT_CLIENT is not None and Constant.MQTT_CLIENT.is_connected():
            Constant.MQTT_CLIENT.publish("device_control", heart_data_json, 0)
        else:
            print(" error mqtt 未连接，无法查询任务、上报心跳、iccid、基站信息")

    def change_platform(self, order_content):
        content = json.loads(order_content, encoding="utf-8")
        if content is not None:
            plantform_url = content.get("plantformURL")
            mqtt_url = content.get("mqttURL")
            if "//" in plantform_url and ":" in plantform_url and "//" in mqtt_url and ":" in mqtt_url:
                Constant.START_SERVICE_URL = plantform_url
                Constant.MQTT_HOST_XXZB = mqtt_url.split("//")[1].split(":")[0]
                Constant.MQTT_PORT_XXZB = int(mqtt_url.split("//")[1].split(":")[1])
                os.system("reboot")

    def on_message(self, rtsp_data):
        print("AEP 收到指令...")
        rtsp_data_json = json.loads(rtsp_data, encoding="utf-8")
        orderType = rtsp_data_json.get("orderType")
        if "bt0303" == orderType:
            self.upgrade(rtsp_data_json.get("orderContent"))
        elif "bt0302" == orderType:
            print("重启")
            os.system("reboot")
        elif "bt0309" == orderType:
            self.change_platform(rtsp_data_json.get("orderContent"))
        rtsp_data_str_en = rtsp_data_json.get("data")
        rtsp_data_str = DESUtils.decrypt(rtsp_data_str_en)
        rtsp_data_json = json.loads(rtsp_data_str, encoding="utf-8")
        if rtsp_data_json is not None:
            print(rtsp_data_str)
            if "query_task" == rtsp_data_json.get("action"):
                self.query_task_back(rtsp_data_json)
            elif "play" == rtsp_data_json.get("action"):
                self.play(rtsp_data_json)
            elif "control" == rtsp_data_json.get("action"):
                self.control_volume(rtsp_data_json)
            elif "play_stop" == rtsp_data_json.get("action"):
                self.stop(rtsp_data_json)
            # elif "upgrade" == rtsp_data_json.get("action"):
            #     self.upgrade(rtsp_data_json)
            else:
                print("未知指令 >>>>>>>>>> " + str(rtsp_data_json))
