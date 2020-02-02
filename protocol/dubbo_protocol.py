#!/usr/bin/env python
# -*- coding: utf-8 -*-


import telnetlib
import time
from locust import events


class Dubbo(telnetlib.Telnet):

    prompt = 'dubbo>'
    __encoding = "utf-8"
    __connect_timeout = 3
    __read_timeout = 10

    def __init__(self, host, port,timeout=__connect_timeout):
        try:
            super().__init__(host, port,timeout)
        except Exception as err:
            print("[host:%s port:%s] 连接失败" % (self.host, self.port))
        else:
            print("*****  [host:%s port:%s] 连接成功  *****" % (self.host, self.port))
            self.write(b"\n")


    def command(self,  str_=""):
        data = self.read_until(Dubbo.prompt.encode())
        self.write(str_.encode() + b"\n")
        return data


    def do_invoke(self, service_name, method_name, param = ''):
        command_str = "invoke {0}.{1}({2})".format(
            service_name, method_name, param)
        self.command(command_str)
        data = self.command("")
        data = data.decode(Dubbo.__encoding,errors='ignore').split('\n')[0].strip()
        return data





class DubboClient(Dubbo):
    def __init__(self, host, port):
        super().__init__(host, port)



    def invoke(self, service_name, method_name, param = ''):
        start_time = time.time()
        try:
            data = self.do_invoke(service_name,method_name,param)
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type="dubbo", name="start",
                                        response_time=total_time, exception=e, response_length = 16333)
        else:
            total_time = int((time.time() - start_time) * 1000)
            events.request_success.fire(request_type="dubbo", name="start",
                                        response_time=total_time, response_length=len(data))

            return data






if __name__ == '__main__':
    onn = DubboClient('192.168.20.4', 23888)

    data = onn.invoke('com.biz.soa.service.promotion.backend.presale.SoaPromotionPreSaleService','findPreSaleAgreement')
    print(data)
    data = onn.invoke('com.biz.soa.service.promotion.backend.presale.SoaPromotionPreSaleService','findPreSaleAgreement')
    print(data)


#
# import json
# import socket
# import telnetlib
#
#
# class dubbo:
#     # 定义私有属性
#     __encoding = "gbk"
#     __finish = 'dubbo>'
#     __connect_timeout = 10
#     __read_timeout = 10
#
#     # 定义构造方法
#     def __init__(self, host, port):
#         self.host = host
#         self.port = port
#         if host is not None and port is not None:
#             self.__init = True
#
#     def set_finish(self, finish):
#         '''
#         defualt is ``dubbo>``
#         '''
#         self.__finish = finish
#
#     def set_encoding(self, encoding):
#         '''
#         If ``result retured by dubbo`` is a ``str`` instance and is encoded with an ASCII based encoding
#         other than utf-8 (e.g. latin-1) then an appropriate ``encoding`` name
#         must be specified. Encodings that are not ASCII based (such as UCS-2)
#         are not allowed and should be decoded to ``unicode`` first.
#         '''
#         self.__encoding = encoding
#
#     def set_connect_timeout(self, timeout):
#         '''
#         Defines a timeout for establishing a connection with a dubbo server.
#         It should be noted that this timeout cannot usually exceed 75 seconds.
#
#         defualt is ``10``
#         '''
#         self.__connect_timeout = timeout
#
#     def set_read_timeout(self, timeout):
#         '''
#         Defines a timeout for reading a response expected from the dubbo server.
#
#         defualt is ``10``
#         '''
#         self.__read_timeout = timeout
#
#     def do(self, command):
#         # 连接Telnet服务器
#         try:
#             tn = telnetlib.Telnet(host=self.host, port=self.port, timeout=self.__connect_timeout)
#         except socket.error as err:
#             print("[host:%s port:%s] %s" % (self.host, self.port, err))
#             return
#
#         # 触发doubble提示符
#         tn.write('\n')
#
#         # 执行命令
#         tn.read_until(self.__finish, timeout=self.__read_timeout)
#         tn.write('%s\n' % command)
#
#         # 获取结果
#         data = ''
#         while data.find(self.__finish) == -1:
#             data = tn.read_very_eager()
#         data = data.split("\n")
#         data = json.loads(data[0], encoding=self.__encoding)
#
#         tn.close()  # tn.write('exit\n')
#
#         return data
#
#     def invoke(self, interface, method, param):
#         cmd = "%s %s.%s(%s)" % ('invoke', interface, method, param)
#         return self.do(cmd)
#
#
# def connect(host, port):
#     return dubbo(host, port)
#
#
# if __name__ == '__main__':
#     Host = '192.168.20.4'  # Doubble服务器IP
#     Port = 23888  # Doubble服务端口
#
#     # 初始化dubbo对象
#     conn = dubbo(Host, Port)
#
#     # 设置telnet连接超时时间
#     conn.set_connect_timeout(10)
#
#     # 设置dubbo服务返回响应的编码
#     conn.set_encoding('gbk')
#
#     interface = 'com.biz.soa.service.promotion.backend.game.GameBaseConfigDubboService'
#     method = 'getCurrentConfig'
#     param = ''
#     print(conn.invoke(interface, method, param))
#
#     command = 'invoke com.biz.soa.service.promotion.backend.game.GameBaseConfigDubboService.getCurrentConfig())'
#     print(conn.do(command))
