# encoding=utf-8

import os, json
import configparser


# 判断文件和文件夹是否存在
def exists(file_path_or_dir_path):
    if os.path.exists(file_path_or_dir_path):
        return True
    else:
        return False


# 写入json数据到文件
def write_json_data(file_path, json_str):
    with open(file_path, 'w') as cf:
        cf.write(json.dumps(json_str))


def write_dns(file_path, dns1, dns2):
    if not exists(file_path):
        fd = open(file_path, "w")
        fd.close()
    with open(file_path, "r+") as resolv:
        data = resolv.read()
        print("resolv.conf : "+str(data))
        if dns1 is not None and dns1 not in data:
            resolv.write("nameserver " + dns1 + "\n")
        if dns2 is not None and dns2 not in data:
            resolv.write("nameserver " + dns2 + "\n")


# 从文件读取json数据
def read_json_data(file_path):
    with open(file_path, 'r') as rf:
        souce_data = rf.read()
    # souce_data = eval(souce_data)
    conf_json = json.loads(souce_data)
    return conf_json


def get_conf(conf_file_name, options, key):
    cf = configparser.ConfigParser()
    cf.read(conf_file_name)
    conf = cf.get(options, key)
    return conf


def set_conf(conf_file_name, section, key, value):
    cf = configparser.ConfigParser()
    cf.read(conf_file_name)
    if not cf.sections():
        cf.add_section(section)
    cf.set(section, key, value)
    cf.write(open(conf_file_name, 'w'))
