# -*- encoding: utf8 -*-
import xlrd
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

data = xlrd.open_workbook('excel/1.xls')

# 通过索引顺序获取
table = data.sheets()[0]
# table = data.data.sheet_by_index(0)
row = table.nrows
col = table.ncols
for i in range(row):
    # print table.row_values(i)
    for key, val in enumerate(table.row_values(i)):
        if u'成交方式' in str(val).decode():
            print u'成交方式', table.row_values(i+1)[key]
        if u'运抵国(地区)' in str(val).decode():
            print u'运抵国(地区)', table.row_values(i + 1)[key]
        if u'贸易方式' in str(val).decode():
            print u'贸易方式', table.row_values(i + 1)[key]
