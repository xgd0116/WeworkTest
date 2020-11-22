# -*- coding:utf8 -*-
import os
import yaml
import requests
import configparser
import time

class Utils:
    def __init__(self):
        self.conf = configparser.ConfigParser()
        # 获取当前文件的路径
        self.parent_dir = os.path.dirname(os.path.abspath(__file__))
        self.conf.read(self.parent_dir + "/access_token.ini")

    @staticmethod
    def get_access_token(corp_id, corp_secret):
        """
        获取AccessToken
        请求方式： GET（HTTPS）
        请求地址： https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
        :return:
        """
        request_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"
        return requests.get(request_url).json()['access_token']

    def read_ini_file(self, section, name):
        """
        读取ini配置文件内容
        :return:
        """
        return self.conf.get(section, name)

    def update_ini_file(self, section, name, value:str):
        """
        更新ini配置文件内容
        :return:
        """
        self.conf.set(section, name, value)
        self.conf.write(open("./access_token.ini", "w+"))

    def get_yaml(self, sec, key):
        with open(self.parent_dir + "/user.yml", encoding="utf-8") as fp:
            result = yaml.load(fp, Loader=yaml.FullLoader)
            result_list = result[sec][key]
            data_list = []
            for i in result_list:
                value_list = []
                for key, value in i.items():
                    value_list.append(value)
                data_list.append(tuple(value_list))
            print(data_list)
            return data_list


    def update_user_token_ini(self, section, token_name, time_name, corp_id, corp_secret):
        """
        更新token和token时间
        :return:
        """
        access_token = self.get_access_token(corp_id, corp_secret)
        now_time = time.time()
        self.update_ini_file(section, token_name, access_token)
        self.update_ini_file(section, time_name, str(now_time))

    def get_user_access_token(self):
        """
        获取成员token
        :return:
        """
        section = "member"
        token_name = "access_token"
        time_name = "token_time"
        corp_id = "ww8de7ba79872d3902"
        corp_secret = "rrOe-DgSIfRdWDlMtKXmnuaufAnQtK7IQ6jMq9qQ1Mk"
        if self.read_ini_file(section, token_name) == "None" or self.read_ini_file(section, time_name) == "None":
            # 当token和token有效时间为None时，重新获取
            self.update_user_token_ini(section, token_name, time_name, corp_id, corp_secret)
        else:
            # 当token过期时，重新获取token（通过当前时间减去上一次获取token的时间，大于7200s，则token过期）
            token_time = self.read_ini_file(section, time_name)
            if (time.time() - float(token_time)) > 7200:
                self.update_user_token_ini(section, token_name, time_name, corp_id, corp_secret)
        return self.read_ini_file(section, token_name)

if __name__=='__main__':
    print(Utils.get_yaml("User", "data"))


