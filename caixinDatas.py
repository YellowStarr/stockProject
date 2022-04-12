# -*- coding: utf-8 -*-
'''
@File     : caixinDatas.py
@Copyright: Qiuwenjing
@Date     : 2021/10/11
@Desc     : 财新个股数据查询获取，写到excel中
'''
import requests
from pandas import DataFrame
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import time,datetime
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
        self._index = []
        self.CN_df = ''

    def get_finacekpi(self, code):

        uri = "/api/stock/cgi/stockFinanceKpiReport"
        param = {
            "code": code,
            "types": "0,1,2,3,4"
        }
        r = requests.get(self.url+uri, params=param, headers=self.head_str, verify=False)
        res = r.json()
        kpis = res['data']
        print(kpis)
        self.get_index(NameSwitch.FINACEKPI)
        self.CN_df = self.get_CN(NameSwitch.FINACEKPI)
        return kpis
        # df = self.turnToPandas(kpis, _index)

    def get_profit(self, code):
        uri = "/api/stock/cgi/stockFinanceProfReport"
        param = {
            "code": code,
            "types": "0,1,2,3,4"
        }
        r = requests.get(self.url + uri, params=param, headers=self.head_str, verify=False)
        res = r.json()
        kpis = res['data']

        self.get_index(NameSwitch.PROFITREPORT)
        self.CN_df = self.get_CN(NameSwitch.PROFITREPORT)
        return kpis

    def get_Debt(self, code):
        uri = "/api/stock/cgi/stockFinanceDebtReport"
        param = {
            "code": code,
            "types": "0,1,2,3,4"
        }
        r = requests.get(self.url + uri, params=param, headers=self.head_str, verify=False)
        res = r.json()
        kpis = res['data']
        self.get_index(NameSwitch.FINACEDEBT)
        self.CN_df = self.get_CN(NameSwitch.FINACEDEBT)
        return kpis

    def get_CashFlow(self, code):
        uri = "/api/stock/cgi/stockFinanceCashflowReport"
        param = {
            "code": code,
            "types": "0,1,2,3,4"
        }
        r = requests.get(self.url + uri, params=param, headers=self.head_str, verify=False)
        res = r.json()
        kpis = res['data']
        self.get_index(NameSwitch.CASHFLOW)
        self.CN_df = self.get_CN(NameSwitch.CASHFLOW)
        return kpis

    def turnToPandas(self, responseData):
        ''''''
        df_origin = {}

        for y in range(len(responseData)):
            # 时间戳转换成日期
            time_stamp = float(responseData[y]["endDate"])
            time_stamp = time_stamp/1000.0
            datetime_array = time.localtime(time_stamp)
            other_way_time = time.strftime("%Y-%m-%d", datetime_array)

            responseData[y]["endDate"] = other_way_time
            # 组装dict
            df_origin[responseData[y]["endDate"]] = responseData[y]
        df = DataFrame(df_origin, index=self._index)
        m_df = self.CN_df.join(df, how='right')
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

    def get_index(self, dict):
        self._index = dict.keys()


if __name__ == "__main__":
    _filepath = "f:\\Python\\stockProject\\finance\\xinlitai_finacedebt.xlsx"
    s = caiXinDatas()
    # data = s.get_finacekpi("101000457")
    # print(data["netProfit"])
    # data1 = s.get_profit("101000835")
    data2 = s.get_Debt("101000835")
    # data3 = s.get_CashFlow("101000457")
    kpi_df = s.turnToPandas(data2)
    # cashflow_df = s.turnToPandas(data3)
    # netprofi = kpi_df.ix["netProfit"][1:] / 10000
    # netprofit_r = kpi_df.ix["netProfitRate"][1:]



    # print(netprofi)
    s.writeToExcel(kpi_df, _filepath)

    # netprofi.plot()
    # netprofit_r.plot()
    # plt.show()

