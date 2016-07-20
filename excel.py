# -*- encoding: utf8 -*-
import xlrd
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

data = xlrd.open_workbook('excel/1.xls')

table = data.sheets()[0]
row = table.nrows
col = table.ncols
for i in range(row):
    for key, val in enumerate(table.row_values(i)):
        if u'成交方式' in str(val):
            print u'成交方式', table.row_values(i + 1)[key]
        if u'运抵国(地区)' in str(val):
            print u'运抵国(地区)', table.row_values(i + 1)[key]
        if u'贸易方式' in str(val):
            print u'贸易方式', table.row_values(i + 1)[key]
