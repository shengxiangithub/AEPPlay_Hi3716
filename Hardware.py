# encoding=utf-8
from ctypes import *
import Constant, FileUtil
import os, time, threading, subprocess


# GPIO2_7  音频输出使能 1、ON  0、OFF
# GPIO0_1  4G电源       1、ON   0、OFF
# GPIO0_4  输出电源控制 1、输出（开机的时候就要设为输出）
# GPIO0_2  状态灯
# GPIO1_2  复位检测

# 打开功放电源
def init(main_obj):
    try:
        gkl = CDLL("libgkl.so")
        Constant.wtire_gpio = gkl.gpio_write
        Constant.wtire_gpio(4, 1)
        print("check_thread start")
        check = threading.Thread(target=check_thread, args=[main_obj], name="check_thread")
        check.start()
        read_serial_thread = threading.Thread(target=read_serial, name="read_serial_thead")
        read_serial_thread.start()
        switch_voice(False)
        switch_4g(main_obj)
    except Exception as e:
        print("硬件初始化失败:" + str(e))


def wait_sn_mac_info():
    gkl = CDLL("libgkl.so")
    Constant.wtire_gpio = gkl.gpio_write
    Constant.wtire_gpio(4, 1)
    Constant.wtire_gpio(2, 1)
    try:
        update_complete_play()  # U盘升级完成，播放提示音
    except Exception as e:
        print("播放升级完成提示音异常：" + str(e))


def update_complete_play():
    update_play_thread = threading.Thread(target=update_play, name='update_play_thread')
    update_play_thread.start()


def update_play():
    switch_voice(True)
    cmd = "mplayer -af volume=-35 -vo null  -ac ffmp3 update_complete.mp3"
    popen = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE)
    popen.wait()
    switch_voice(False)


def wait_conf_info():
    gkl = CDLL("libgkl.so")
    Constant.wtire_gpio = gkl.gpio_write
    Constant.wtire_gpio(2, 1)
    time.sleep(2)
    Constant.wtire_gpio(2, 0)


def read_serial():
    try:
        while not Constant.input_flag:  # 不允许输入命令
            value = input("")
            print(value)
            if "betel_" in value:
                os.system(value.replace("betel_", ""))
            elif "serialwrite" in value:
                value = value.replace("serialwrite", "").replace(" ", "").replace("\"", "").replace("'", "")
                if value is not None:
                    FileUtil.set_conf(Constant.SERIAL_MAC_PATH, "sn_mac", "SN", value)
                    print("\n===SN OK !\n")
            elif "writemac" in value:
                value = value.replace("writemac", "").replace(" ", "").replace("\"", "").replace("'", "")
                if value is not None:
                    FileUtil.set_conf(Constant.SERIAL_MAC_PATH, "sn_mac", "MAC", value)
                    print("\n===MAC OK\n")
            elif "reboot" in value:
                os.system("reboot")
            elif "get_sn" in value:
                try:
                    sn = FileUtil.get_conf(Constant.SERIAL_MAC_PATH, "sn_mac", "SN")
                    print("get_sn:" + str(sn))
                except Exception as e:
                    print("get_sn: error" + str(e))
            elif "get_mac" in value:
                try:
                    mac = FileUtil.get_conf(Constant.SERIAL_MAC_PATH, "sn_mac", "MAC")
                    print("get_mac:" + str(mac))
                except Exception as e:
                    print("get_mac: error" + str(e))
            elif "get_imei" in value:
                cmd = 'echo "AT+SIMEI?" > /dev/ttyUSB2 & timeout -t 1 cat /dev/ttyUSB2 | grep SIMEI '
                os.system(cmd)
            elif "get_csq" in value:
                cmd = 'echo "AT+CSQ" > /dev/ttyUSB2  & timeout -t 3 cat /dev/ttyUSB2 | grep CSQ:'
                os.system(cmd)
            elif "check_usb" in value:
                cmd = 'cat /mnt/sda1/usb_check.txt'
                os.system(cmd)
            elif "get_device_status" in value:
                if Constant.MQTT_CLIENT is not None and Constant.MQTT_CLIENT.is_connected():
                    print("status: online")
                else:
                    print("status: offline")
            elif "test_play" in value:
                Constant.wtire_gpio(4, 1)
                Constant.wtire_gpio(2, 1)
                try:
                    update_complete_play()  # U盘升级完成，播放提示音
                except Exception as e:
                    print("播放升级完成提示音异常：" + str(e))
                print("test_play: ing")
            elif "mute" in value:
                switch_voice(False)
                print("mute: ok")
            elif "unm_ute" in value:
                switch_voice(True)
                print("unmute: ok")
            elif "power_off" in value:
                Constant.wtire_gpio(4, 0)
                print("power_off:ok")
            elif "power_on" in value:
                Constant.wtire_gpio(4, 1)
                print("power_on:ok")
    except Exception as e:
        print("read_serial failed : " + str(e))
        time.sleep(10)
        read_serial()


def check_thread(main_obj):
    for i in range(1500):
        Constant.wtire_gpio(2, 1)
        time.sleep(Constant.time_interval)
        Constant.wtire_gpio(2, 0)
        time.sleep(Constant.time_interval)
    if main_obj is not None:
        main_obj.stop_server()
    while True:
        check_network()


def check_network():
    while True:
        if Constant.MQTT_CLIENT is None or not Constant.MQTT_CLIENT.is_connected():  # 如果没网
            if Constant.G4EN:
                print("尝试拨号...")
                os.system('echo "AT\$QCRMCALL=1,1" > /dev/ttyUSB2')
            for i in range(600):  # 等待20分钟
                Constant.wtire_gpio(2, 1)
                time.sleep(Constant.time_interval)
                Constant.wtire_gpio(2, 0)
                time.sleep(Constant.time_interval)
            if Constant.MQTT_CLIENT is None or not Constant.MQTT_CLIENT.is_connected():  # 如果依然没网
                os.system("reboot")
        else:
            if Constant.G4EN:
                get_rsrp_pci_cellid_rssi()
            for i in range(600):  # 等待20分钟后再次检测
                Constant.wtire_gpio(2, 1)
                time.sleep(Constant.time_interval)
                Constant.wtire_gpio(2, 0)
                time.sleep(Constant.time_interval)
    # TODO 递归次数不能太多



def get_iccid():
    try:
        cmd = 'echo "AT+CCID" > /dev/ttyUSB2 & timeout -t 1 cat /dev/ttyUSB2 | grep CCID'
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        out, err = p.communicate()
        p.wait(1)
        ccid = None
        for line in out.splitlines():
            if line is not None and "+CCID:" in str(line):
                ccid = str(line)
                print(">>>>>>>>>>>1 iccid" + ccid)
                break
        Constant.iccid = str(ccid.replace("+CCID: ", "").replace("b'", "").replace("'", ""))
        print(">>>>>>>>>>>2 iccid" + ccid)
        print("iccid：" + str(Constant.iccid))
    except Exception as e:
        print("获取iccid失败" + str(e))


def get_rsrp_pci_cellid_rssi():
    try:
        cmd = 'echo "AT+CPSI?" > /dev/ttyUSB2 & timeout -t 1 cat /dev/ttyUSB2 | grep CPSI '
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        out, err = p.communicate()
        p.wait(1)
        rsrp_pci_cellid_rssi = None
        for line in out.splitlines():
            if line is not None and "+CPSI:" in str(line) and "LTE" in str(line):
                rsrp_pci_cellid_rssi = str(line)
                break
        rsrp_pci_cellid_rssi = rsrp_pci_cellid_rssi.split(",")
        Constant.rsrp = str(int(int(rsrp_pci_cellid_rssi[11]) / 10))
        Constant.pci = str(rsrp_pci_cellid_rssi[5])
        Constant.ecl = ""
        Constant.cell_id = str(rsrp_pci_cellid_rssi[4])
        Constant.rssi = str(int(int(rsrp_pci_cellid_rssi[12]) / 10))
        print("rsrp:" + Constant.rsrp)
        print("pci:" + Constant.pci)
        print("ecl:")
        print("cell_id：" + rsrp_pci_cellid_rssi[4])
        print("rssi:" + Constant.rssi)
    except Exception as e:
        print("获取基站信息失败" + str(e))


def switch_voice(open_flag):
    if open_flag:
        print("打开声音")
        Constant.wtire_gpio(23, 1)  # 取消静音
    else:
        print("关闭声音")
        Constant.wtire_gpio(23, 0)


def switch_4g(main_obj):
    print("配置MAC:" + str(Constant.MAC))
    mac_cmd = "ifconfig eth0 hw ether " + Constant.MAC + " & ifconfig lo up"
    os.system(mac_cmd)
    time.sleep(2)
    cmd = "ifconfig eth0 " + str(Constant.IP) + " netmask " + str(Constant.IPMASK)
    print(cmd)
    os.system(cmd)
    if main_obj is not None:
        main_obj.start_server_thread()
    if "1" == Constant.G4EN:
        Constant.network = 2
        print("开启4G")
        Constant.wtire_gpio(1, 0)
        time.sleep(3)
        Constant.wtire_gpio(1, 1)
        time.sleep(30)
        os.system('echo "AT\$QCRMCALL=1,1" > /dev/ttyUSB2')
        time.sleep(10)
        os.system("ifconfig wwan0 up")
        time.sleep(2)
        os.system("udhcpc -i wwan0 &")
        print("启用4G完成")
    FileUtil.write_dns(Constant.NAMESERVER_PATH, Constant.DNS1, Constant.DNS2)
    # os.system(Constant.NAMESERVER_PATH)
    cmd = "route add default gw " + Constant.GATEWAY
    print(cmd)
    os.system("route add default gw " + Constant.GATEWAY)
    print("网络配置完成")
