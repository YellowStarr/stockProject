# -*- coding: utf-8 -*-
'''
@File     : caixinDatas.py
@Copyright: Qiuwenjing
@Date     : 2021/10/11
@Desc     : 财新个股数据查询获取，写到excel中
'''
import requests

class caiXinDatas:
    def __init__(self):
        ''''''
        self.head_str = {
            "Host": "s.ccxe.com.cn",
            "Connection": "keep-alive",
            "Accept": "application/json,text/plain,*/*",
            "sec-ch-ua": '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN, zh;q = 0.9",
            "Referer": "https://s.ccxe.com.cn/stock/market",
            "Cookie": "UM_distinctid=17c600894f6905-0e41aa70507805-a7d173c-1fa400-17c600894f7b18; CNZZDATA1279958504=1428887084-1633696438-https%253A%252F%252Fwww.caixin.com%252F%7C1633696438"
        }
        self.url = "https://s.ccxe.com.cn"

    def get_data(self):
        uri = "/market/api/stock/cgi/search"
        param = {
            "keyword": "002294",
            "page":1,
            "size":20
        }
        r = requests.get(self.url+uri, params=param, headers=self.head_str, verify=False)
        print(r.text)

if __name__ == "__main__":
    s = caiXinDatas()
    s.get_data()

