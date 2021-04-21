# from selenium.webdriver import Chrome, ChromeOptions
#
# opt = ChromeOptions()  # 创建Chrome参数对象
# opt.headless = True  # 把Chrome设置成可视化无界面模式，windows/Linux 皆可
# driver = Chrome(options=opt)  # 创建Chrome无界面对象
#
# driver.get('http://www.baidu.com')
# print(driver.current_window_handle)
# print(driver.page_source)
# driver.close()
# -*- coding=utf-8 -*-
import requests


class UNIT:
    def __init__(self, api_key, api_secret):
        self.access_token = None
        self.url = None

        self.set_access_token(api_key, api_secret)

    def set_access_token(self, api_key, api_secret):
        host = 'https://aip.baidubce.com/oauth/2.0/token?' \
               'grant_type=client_credentials&' \
               'client_id={0}&' \
               'client_secret={1}'.format(api_key, api_secret)
        response = requests.post(host)
        if response:
            self.access_token = response.json()['access_token']

    def query(self, query_text):
        self.url = 'https://aip.baidubce.com/rpc/2.0/unit/service/chat?access_token=' + self.access_token
        post_data = """{
                    "bot_session": "",
                    "log_id": "7758521",
                    "service_id": "S29640",	# 你的聊天机器人的ID
                    "request": {
                        "bernard_level": 1,
                        "client_session": "{\\\"client_results\\\":\\\"\\\", \\\"candidate_options\\\": []}",
                        "query": "%s",	# 要查询的文字
                        "query_info": {
                            "asr_candidates": [],
                            "source": "KEYBOARD",
                            "type": "TEXT"
                        },
                        "updates": "",
                        "user_id": "88888"
                    },
                    "session_id": "",
                    "version": "2.0"
                }""" % query_text
        post_data = post_data.encode('utf-8')
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.url, data=post_data, headers=headers)
        if response:
            return response.json()['result']['response_list'][0]['action_list'][0]['say']
