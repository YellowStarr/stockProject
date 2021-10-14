# -*- coding: utf-8 -*-
'''
@File     : operExcel.py
@Copyright: Qiuwenjing
@Date     : 2021/10/14
@Desc     :
'''
import openpyxl

def create_excel(filepath):
    f = openpyxl.Workbook()
    sheet1 = f.active
    f.save(filepath)

