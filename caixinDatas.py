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
        head_str = {
            "Host": "s.ccxe.com.cn",
            "Connection": "keep - alive",
            "Accept": "application/json,text/plain,*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
            "sec-ch-ua-platform": "Windows",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN, zh;q = 0.9",
            "Cookie": "UM_distinctid=17c600894f6905-0e41aa70507805-a7d173c-1fa400-17c600894f7b18; CNZZDATA1279958504=1428887084-1633696438-https%253A%252F%252Fwww.caixin.com%252F%7C1633696438"
        }
