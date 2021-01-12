# encoding = utf - 8
from flask import Flask, render_template, request, jsonify
import time
import json
import FileUtil, Constant
import os

app = Flask(__name__, static_url_path='')
randomNum = "kAOVlC0/z7ojxgJ25LB4i8cwVBW2yQB0e0bpjKTl6VywndATpm6ATv0r6lbguvzMhVHih77I6tpvqQDxGfuf6fVoqgvW3OwI3bohFsL9"


@app.route('/')
def login0():
    # return "<h1>hello, Flask!</h1>"
    return render_template('login.html')


@app.route('/login.html')
def login1():
    return render_template('login.html')


@app.route('/login.do', methods=['GET', 'POST'])
def login():
    # print("login.do  " + str(request.data, encoding="utf-8"))
    form = json.loads(str(request.data, encoding="utf-8"), encoding="utf-8")
    if form.get("u") == "admin" and form.get("p") == "admin":
        return jsonify({'s': 0, "randomNum": randomNum})
    else:
        return jsonify({'s': 1, 'errmsg': '用户名或者密码错误'})


@app.route('/config.html', methods=['GET', 'POST'])
def confightml():
    return render_template('config.html')


@app.route('/config.do', methods=['GET', 'POST'])
def config():
    form = json.loads(str(request.data, encoding="utf-8"), encoding="utf-8")
    print(str(form) + str(randomNum))
    time.sleep(1)
    if form.get("num") == str(randomNum):
        return jsonify({'s': 0, "randomNum": randomNum})
    else:
        return jsonify({'s': 1, "randomNum": randomNum})


@app.route('/btnquery.do', methods=['GET', 'POST'])
def btnquery():
    # form = json.loads(request.data, encoding="utf-8")
    if FileUtil.exists(Constant.CONF_FILE_PATH):
        conf_json = FileUtil.read_json_data(Constant.CONF_FILE_PATH)
        conf_json["s"] = 0
        conf_json["sn"] = Constant.USELESS_SN
        conf_json["mac"] = Constant.MAC
        conf_json["ver"] = "betel smartbox ("+str(Constant.version)+") 2020-03-16 01：10：50"
        return jsonify(conf_json)
    else:
        return jsonify(
            {'s': 0, "ip": "192.168.199.112", "ipmask": "255.255.255.0", "gateway": "192.168.199.1", "mac": Constant.MAC,
             "dns1":"114.114.114.114","dns2":"223.5.5.5",
             "g4en": 1, "mqttep": "tcp://mqtt.ctwing.cn:1883",
             "mqttpass": "HbVdirK0oDI4qQ3Jqmmd5iNK_DoBTN_KNuX6s-7mmAg", "despass": "tywlzhyx",
             "productid": "", "sn": Constant.USELESS_SN, "apnname": "", "apnuser": "", "apnpass": "",
             "ver": "betel smartbox ("+str(Constant.version)+") 2020-03-07 23：52：50"})


@app.route('/btnsave.do', methods=['GET', 'POST'])
def btnsave():
    form = json.loads(str(request.data, encoding="utf-8"), encoding="utf-8")
    print(form)
    try:
        FileUtil.write_json_data(Constant.CONF_FILE_PATH, form)
        return jsonify({'s': 0, "randomNum": randomNum})
    except Exception as e:
        print(str(e))
        return jsonify({'s': 1, "randomNum": randomNum})


@app.route('/btnreboot.do', methods=['GET', 'POST'])
def btnreboot():
    try:
        os.system("reboot")
        return jsonify({'s': 0})
    except Exception as e:
        print(str(e))
        return jsonify({'s': 1})

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=80)
