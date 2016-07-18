# -*- encoding: utf8 -*-
import xlrd

data = xlrd.open_workbook('excel/1.xls')

# 通过索引顺序获取
table = data.sheets()[0]
row = table.nrows
col = table.ncols
for i in range(row):
    for v in table.row_values(i):
        print v