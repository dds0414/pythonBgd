# -*- encoding: utf8 -*-
'''
Created on 2011-12-01
处理doc文件
@author:
'''
from win32com import client  # 将模块加载进来


word = client.Dispatch('Excel.Application')

#word.Visible = 0

# 打开一个已存在的文件
doc = word.Documents.Open(r'excel/1.xls')

# newdoc为新word文件
# newdoc = word.Documents.Add()
# python处理word文件:win32com用法详解
# docC = word.Documents.Count

# 打印doc（第一个word文件）内容，中文不能打,报错
print doc.Content
# python处理word文件:win32com用法详解  #
# range = newdoc.Range(0,0)

# range = newdoc.Range()  # 尾部
# python处理word文件:win32com用法详解  #
# range = newdoc.Range(doc.Content.Strat,doc.Content.end)

# range.InsertBefore('daisy')#在范围前写入字符串
# python处理word文件:win32com用法详解
# range.InsertAfter(doc.Content)

# newdoc.SaveAs(r'D:\b.docx')  # 另存为b.docx（office2010）

# 关闭
doc.Close()
# newdoc.Close()
word.Quit()
