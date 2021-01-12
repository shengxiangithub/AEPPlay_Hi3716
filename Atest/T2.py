# import time
# from multiprocessing import Process
#
#
# def run_forever():
#     while 1:
#         print(time.time())
#         time.sleep(2)
#
#
# def main():
#     p = Process(target=run_forever)
#     p.start()
#     print('start a process.')
#     time.sleep(10)
#     if p.is_alive:
#         # stop a process gracefully
#         p.terminate()
#         print('stop process')
#         p.join()
#
#
# if __name__ == '__main__':
#     for i in range(3):
#         print(i)
#     main()

import FileUtil, os


def waite_write_sn_mac():
    # Hardware.wait_sn_mac_info()
    print("请写入：")
    while True:
        value = input()
        if "serialwrite" in value:
            value = value.replace("serialwrite", "").replace(" ", "")
            if value is not None:
                FileUtil.set_conf("serial_mac.conf", "sn_mac", "SN", value)
                print("write sn ok:" + value)
        elif "writemac" in value:
            value = value.replace("writemac", "").replace(" ", "")
            if value is not None:
                FileUtil.set_conf("serial_mac.conf", "sn_mac", "MAC", value)
                print("write mac ok:" + value)
        elif "reboot" in value:
            os.system("reboot")

    # 初始化配置文件


def init_terminal_conf():
    if not FileUtil.exists("serial_mac.conf"):
        print("未找到sn配置文件")
        waite_write_sn_mac()
    else:
        sn = FileUtil.get_conf("serial_mac.conf", "sn_mac", "SN")
        if sn is None:
            print("有配置文件但是没有SN值")
            waite_write_sn_mac()
        else:
            print(sn)
        mac = FileUtil.get_conf("serial_mac.conf", "sn_mac", "MAC")
        if mac is not None:
            print(mac)


if __name__ == '__main__':
    #init_terminal_conf()
    value = "serialwrite '122331231'".replace("serialwrite", "").replace(" ", "").replace("\"", "").replace("'","")
    print(value)

# import Constant, threading, os,time
#
#
# def read_serial():
#     try:
#         while not Constant.input_flag:  # 不允许输入命令
#             result = os.popen('read')
#             res = result.read()
#             print(res)
#             for line in res.splitlines():
#                 print(str(line))
#                 if "ShengXian" == line:
#                     time.sleep(20)
#                 elif "AdminBetel" == line:
#                     Constant.input_flag = True
#     except Exception as e:
#         print("read_serial failed : " + str(e))
#         time.sleep(10)
#         read_serial
#
#
# if __name__ == '__main__':
#     read_serial_thread = threading.Thread(target=read_serial, name="read_serial_thead")
#     read_serial_thread.start()
