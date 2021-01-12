# b = [1, 2,0, 5, 3, 4, 7, 10,11,9,123,9,9]
# for i in range(len(b)-1):
#     for j in range(len(b)-1-i):
#         if b[j] > b[j + 1]:
#             c = b[j]
#             b[j] = b[j + 1]
#             b[j+1] = c
# print(b)
# import time
# print(int(time.time()))
# time.sleep(3)
# print(int(time.time()))
# from pymqtt import Mqtt
#
# config = {'MQTT_IP': 'xxzb.betelinfo.com"', 'MQTT_PORT': 18883, 'MQTT_USER': '100177430182AD0001',
#           'MQTT_PASSWORD': '100177430182AD0001'}
# fmqtt = Mqtt()
# fmqtt.config_from_obj(config)
#
#
# success = fmqtt.publish('hell world', 'topic', qos=2)
# print(success)
# @fmqtt.subscribe(topic='topic', qos=2)
# def flask_rabmq_test(body):
#     print(body)
#     return True

# import logging
#
# from flask import Flask
#
# from pymqtt import Mqtt
#
# logging.basicConfig(format='%(asctime)s %(process)d,%(threadName)s %(filename)s:%(lineno)d [%(levelname)s] %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     level=logging.INFO)

# logger = logging.getLogger(__name__)
#
# app = Flask(__name__)
#
# app.config.setdefault('MQTT_IP', 'xxzb.betelinfo.com')
# app.config.setdefault('MQTT_PORT', 18883)
# app.config.setdefault('MQTT_USER', '100177430182AD0001')
# app.config.setdefault('MQTT_PASSWORD', '100177430182AD0001')
#
# fmqtt = Mqtt()
# fmqtt.config_from_obj(app.config)
#
#
# @app.route('/')
# def hello_world():
#     content = 'hello world'
#     success = fmqtt.publish('hell world', 'topic', qos=2)
#     return 'send %s success %s' % (content, success)
#
#
# @fmqtt.subscribe(topic='topic', qos=2)
# def flask_rabmq_test(body):
#     logger.info(body)
#     return True
#
#
# if __name__ == '__main__':
#     fmqtt.run()
#     app.run()


#
# s = "-" + str(int(50 - (x/ 2)*0.6))
# print(s)
# import serial  # 导入模块
#
# import serial.tools.list_ports
#
# port_list = list(serial.tools.list_ports.comports())
# print(port_list)
# if len(port_list) == 0:
#     print('无可用串口')
# else:
#     for i in range(0, len(port_list)):
#         print(port_list[i])
#
# try:
#     # 端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
#     portx = "COM7"
#     # 波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
#     bps = 115200
#     # 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
#     timex = 5
#     # 打开串口，并得到串口对象
#     ser = serial.Serial(portx, bps, timeout=timex)
#
#     # 写数据
#     result = ser.write("我是东小东".encode("gbk"))
#     print("写总字节数:", result)
#
#     ser.close()  # 关闭串口
#
# except Exception as e:
#     print("---异常---：", e)
import Constant


def get_csq():
    try:
        # cmd = 'echo "AT+CSQ" > /dev/ttyUSB2  & timeout -t 1 cat /dev/ttyUSB2 | grep CSQ:'
        # p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        # out, err = p.communicate()
        # p.wait(2)
        # csq = None
        # for line in out.splitlines():
        #     if line is not None and "CSQ:" in str(line) and "," in str(line) and " " in str(line):
        #         csq = str(line)
        #         break
        csq = '+CSQ: 29,99'
        csq = int(csq.split(" ")[1].split(",")[0])
        # if csq < 10:
        #     Constant.RSSI = 0
        # elif csq < 15:
        #     Constant.RSSI = 1
        # elif csq < 20:
        #     Constant.RSSI = 2
        # elif csq < 23:
        #     Constant.RSSI = 3
        # elif csq < 26:
        #     Constant.RSSI = 4
        # elif csq < 32:
        #     Constant.RSSI = 5
        # else:
        #     Constant.RSSI = csq
        Constant.RSSI = csq * 2 - 113
        print("信号强度：" + str(Constant.RSSI))
        cpsi = "+CPSI: LTE,Online,460-11,0x400B,67286066,241,EUTRAN-BAND3,1825,4,4,-87,-896,-625,14"
        cpsi = cpsi.split(",")
        for i in range(len(cpsi)):
            print(str(i) + "      " + cpsi[i])
        print(int(-625 / 10))

        print("RSRP:" + cpsi[11])
        print("PCI:" + cpsi[5])
        print("ecl:")
        print("cell_id：" + cpsi[4])
        rssi = int(cpsi[12]) / 10
        print("rssi:" + str(rssi))
    except Exception as e:
        print("获取信号强度失败" + str(e))


if __name__ == '__main__':
    #get_csq()
    iccid = "b'89860318250250426011'".replace("b'", "").replace("'", "")
    i=-89.599999999999994
    print(int(i))
    print(iccid)

