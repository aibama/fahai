

import sys

import xlwt
"""
Created on Sun Oct  1 10:08:49 2017

@author: dzs

#Description:xls 操作接口

"""


def WriteSheetRow(sheet,rowValueList,rowIndex,isBold):

	i = 0

	style = xlwt.easyxf('font: bold 1')

	#style = xlwt.easyxf('font: bold 0, color red;')#红色字体

	#style2 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow; font: bold on;') # 设置Excel单元格的背景色为黄色，字体为粗体

	for svalue in rowValueList:

		#strValue = unicode(str(svalue),'utf-8')

		if isBold:

			sheet.write(rowIndex,i,svalue,style)

		else:

			sheet.write(rowIndex,i,svalue)

		i = i + 1

def save_Excel(strFile,valueList,headList=""):
	#excelFile = unicode(strFile, "utf8")

	wbk = xlwt.Workbook()

	sheet = wbk.add_sheet('sheet1',cell_overwrite_ok=True)

	rowIndex = 0

	#写入head
	if headList != "":
		WriteSheetRow(sheet,headList,rowIndex,True)
	for i in valueList:
		WriteSheetRow(sheet,i,rowIndex,True)
		rowIndex = rowIndex+1
	wbk.save(strFile)