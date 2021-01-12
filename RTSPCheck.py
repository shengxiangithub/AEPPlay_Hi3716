import socket
from urllib.parse import urlparse

config_dict = {
    'cseq': 2,
    'user_agent': 'LibVLC/3.0.2 (LIVE555 Streaming Media v2016.11.28)',
    'timeout': 30,
    'recvbite': 4096,
    'res_status': '200 OK',
    'rtsp_status': 'flase'
}

clientports = [60784, 60785]


def options_get(url):
    '''
    options请求检测
    url: rtsp流地址
    return: options请求相应
    '''
    url = urlparse(url)
    host = url.netloc
    hostname = url.hostname
    path = url.path
    port = url.port
    str_options = 'OPTIONS rtsp://' + str(host) + \
                  path + ' RTSP/1.0\r\n'
    str_options += 'CSeq: ' + str(config_dict['cseq']) + '\r\n'
    str_options += 'User-Agent: ' + config_dict['user_agent'] + '\r\n'
    str_options += '\r\n'
    print(str_options)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(config_dict['timeout'])
    client.connect((hostname, port))
    client.send(str_options.encode())
    d = client.recv(config_dict['recvbite'])
    return d


def describe_get(url):
    '''
    describe请求检测
    url: rtsp流地址
    return: describe请求相应
    '''
    url = urlparse(url)
    host = url.netloc
    hostname = url.hostname
    path = url.path
    port = url.port
    str_describe = 'DESCRIBE rtsp://' + str(host) + \
                   path + ' RTSP/1.0\r\n'
    str_describe += 'CSeq: ' + str(config_dict['cseq'] + 1) + '\r\n'
    str_describe += 'User-Agent: ' + config_dict['user_agent'] + '\r\n'
    str_describe += '\r\n'
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(config_dict['timeout'])
    client.connect((hostname, port))
    client.send(str_describe.encode())
    d = client.recv(config_dict['recvbite'])
    return d


def setup_get(url):
    '''
    setup请求检测
    url: rtsp流地址
    return: setup请求相应
    '''
    url = urlparse(url)
    host = url.netloc
    hostname = url.hostname
    path = url.path
    port = url.port
    str_setup = 'SETUP rtsp://' + str(host) + path + '/' + 'streamid=0' + ' RTSP/1.0\r\n'
    str_setup += 'CSeq: ' + str(config_dict['cseq'] + 2) + '\r\n'
    str_setup += 'User-Agent: ' + config_dict['user_agent'] + '\r\n'
    # config_dict['user_agent']
    str_setup += 'Transport: RTP/AVP;unicast;client_port=61740-61741\r\n\r\n'
    str_setup += '\r\n'
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(config_dict['timeout'])
    client.connect((hostname, port))
    client.send(str_setup.encode())
    d = client.recv(config_dict['recvbite'])
    return d


def teardown_get(url):
    '''
    teardown请求检测
    url: rtsp流地址
    return: teardown请求相应
    '''
    url = urlparse(url)
    host = url.netloc
    hostname = url.hostname
    path = url.path
    port = url.port
    str_teardown = 'TEARDOWN rtsp://' + str(host) + path + ' RTSP/1.0\r\n'
    str_teardown += 'CSeq: ' + str(config_dict['cseq'] + 4) + '\r\n'
    str_teardown += 'User-Agent: ' + config_dict['user_agent'] + '\r\n'
    str_teardown += '\r\n'
    print(str_teardown)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(config_dict['timeout'])
    client.connect((hostname, port))
    client.send(str_teardown.encode())
    d = client.recv(config_dict['recvbite'])
    return d


def send_main(url):
    try:
        str_options = str(options_get(url))
        print(str_options)
        if config_dict['res_status'] in str_options:
            str_des = str(describe_get(url))
            print(str_des)
            if config_dict['res_status'] in str_des:
                str_setup = str(setup_get(url))
                str_teardown = str(teardown_get(url))
                print(str_setup)
                print(str_teardown)
                if config_dict['res_status'] in str_teardown:
                    config_dict['rtsp_status'] = 'true'
                    return True
    except Exception as e:
        print(e)
        return False
    else:
        return False

#rtsp://14.29.242.109:10054/3200000174a370728bc0f53a3b509c62a84db7df0000.sdp
#rtsp://14.29.204.2:10054/320000011b538997c38be53cbd45b5b604cef3130000.sdp
#rtsp://14.29.242.109:10054/3200000174a370728bc0f53a3b509c62a84db7df0000.sdp
#print(send_main('rtsp://14.29.242.109:10054/3200000174a370728bc0f53a3b509c62a84db7df0000.sdp'))
