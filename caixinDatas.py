# -*- coding: utf-8 -*-
'''
@File     : caixinDatas.py
@Copyright: Qiuwenjing
@Date     : 2021/10/11
@Desc     : 财新个股数据查询获取，写到excel中
'''
import requests
from pandas import DataFrame
import pandas as pd
import os
from utils import operExcel, NameSwitch

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
        self._index = ["assetLiabilityRatio", "basicEarningsPerShare", "capitalReservePerShare",
                  "dilutedEarningsPerShare", "evEbit",
                  "evEbitda", "grossProfitMargin", "netAssetsPerShare", "netProfit", "netProfitRate",
                  "netProfitYoyGrowthRate", "operCashflowPerShare",
                  "operIncome", "operIncomeYoyGrowthRate", "priceBookRatio", "priceEarningRatio", "salesMargin",
                  "undistributedProfitPerShare", "weightedRoe"]

    def get_finacekpi(self, code):

        uri = "/api/stock/cgi/stockFinanceKpiReport"
        param = {
            "code": code,
            "types": "0,1,2,3,4"
        }
        r = requests.get(self.url+uri, params=param, headers=self.head_str, verify=False)
        res = r.json()
        kpis = res['data']
        return kpis
        # df = self.turnToPandas(kpis, _index)

    def turnToPandas(self, responseData, CN_df):
        ''''''
        df_origin = {}
        for y in range(len(responseData)):
            # 组装dict
            df_origin[responseData[y]["financeTime"]] = responseData[y]
        df = DataFrame(df_origin, index=self._index)
        m_df = CN_df.join(df, how='right')
        return m_df


    def writeToExcel(self, df, filepath):
        isExist = os.path.exists(filepath)
        if isExist:
            df.to_excel(filepath)
        else:
            operExcel.create_excel(filepath)
            df.to_excel(filepath)
        return df

    def get_CN(self, dict):
        new_Dict = {'CN': dict}
        df = DataFrame(new_Dict)
        return df

if __name__ == "__main__":
    _filepath = "f:\\Python\\stockProject\\finance\\shede.xlsx"
    s = caiXinDatas()
    data = s.get_finacekpi("101000835")
    CN_df = s.get_CN(NameSwitch.FINACEKPI)
    df = s.turnToPandas(data,CN_df)
    s.writeToExcel(df, _filepath)

