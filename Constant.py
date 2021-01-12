# ecoding=utf-8
version = "8.0.5"
CONF_FILE_PATH = "/root/terminal_config.txt"
# CONF_FILE_PATH = "E:\\Workspace\\Python\\web\\terminal_config.txt"
NAMESERVER_PATH = "/var/resolv.conf"
SERIAL_MAC_PATH = "/db/serial_mac.conf"
msg_queue = None
wtire_gpio = None
# 以下数据读取自 CONF_FILE_PATH
IP = "192.168.199.12"
IPMASK = "255.255.255.0"
GATEWAY = "192.168.199.1"
DNS1 = "114.114.114.114"
DNS2 = "223.5.5.5"
MAC = ""
G4EN = "1"
# DES_KEY = "tywlzhyx"
# MQTT_HOST = "mqtt.ctwing.cn"
# MQTT_PORT = 1883
# SN = "100177440183IP0002"
# PWD = "EG6Rv0d5bXSFv48PorNp4ZzKK2dPhj-EQPhqNkcEh5c"
DES_KEY = ""
MQTT_HOST = ""
MQTT_PORT = None
SN = ""
PWD = ""
MQTT_CLIENT = None
USELESS_SN = ""

MQTT_HOST_XXZB = "58.213.162.165"  # tcp://58.213.162.165:18883
MQTT_PORT_XXZB = 1883
START_SERVICE_URL = "http://58.213.162.165:9002"  # http://58.213.162.165:9012
MQTT_CLIENT_XXZB = None

STATUS = 1  # 设备状态 1：待机 2：播放
TASK_NUM = ""
VOLUME = 80  # 音量 0-100

network = 1  # 1:有线，2:4G

time_interval = 0.3

input_flag = False

rsrp = ""
pci = ""
ecl = ""
cell_id = ""
rssi = "0"
iccid = ""

PAUSE_FLAG = False  # 暂停任务，不删除
CANCLE_FLAG = False  # 取消任务
