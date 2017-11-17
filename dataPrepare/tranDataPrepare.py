import re
import json
import demjson

import logging

import simplejson

from xlsMulipulate import save_Excel

"""
对DATA_RESULT数据进行处理，供预训练使用
"""

file_dir = r"C:\Users\Administrator\PycharmProjects\ltptest2\DATA\DATA_T_RESULT.txt"
fuXLSfile_dir = r"C:\Users\Administrator\PycharmProjects\ltptest2\DATA\neg.xls"
zhengXLSfile_dir = r"C:\Users\Administrator\PycharmProjects\ltptest2\DATA\pos.xls"
zhongXLSfile_dir = r"C:\Users\Administrator\PycharmProjects\ltptest2\DATA\zhong.xls"

logger = logging.getLogger('root')

def fileread():
	fin = open(file_dir, 'r',encoding='UTF-8')
	line = fin.read()
	return line

class tranData():
	"""
	#返回一个item 给项目用
	#带异常处理
	"""
	def dataPrepare(self):
		pattern = r'\[(.+?)\]'
		content = repr(fileread())
		regex = re.compile(pattern)
		findItems = regex.findall(content)
		# def specifyData(regex):
		# 	for i in regex:
		# 		pattern = r'\[(.+?)\]'
		# 		regex = re.compile(pattern)
		# 		yield re.compile(i)
		# dictFordata = None
		# for i in specifyData(regex):
		# 	#不用转成dict 因为格式形如{"":"","":""}
		# 	yield i
		for i in findItems:
			pattern = r'\{(.+?)\}'
			regex = re.compile(pattern)
			findEven = regex.findall(i)
			yield findEven
			
	"""
	#正向反向中性保存数据到文档，如果没有digest；则保存name
	#
	"""
	def dataToFile(self):
		poslist = []
		neglist = []
		zhongxinglist = []
		k = self.dataPrepare()
		for i in self.dataPrepare():
			#if i['eventLevel'] == '负向':
			events = k.__next__()
			for event in events:
				eventplus = '{'+event+'}'
				dictForEvent = simplejson.loads(eventplus)
				print(dictForEvent)
				print(type(dictForEvent))
				if dictForEvent['eventLevel'] == "正向":
					poslist.append(event)
				if dictForEvent['eventLevel'] == "负向":
					neglist.append(event)
				if dictForEvent['eventLevel'] == "中性":
					zhongxinglist.append(event)
		# save_Excel(fuXLSfile_dir,neglist)
		# save_Excel(zhengXLSfile_dir,poslist)
		# save_Excel(zhongXLSfile_dir,poslist)
		print(poslist.__len__())
		print(neglist.__len__())
		print(zhongxinglist.__len__())


if __name__ == "__main__":
	d = tranData()
	k = d.dataToFile()
	for i in range(10):
		#print(k.__next__())
		#每个evens都有很多even，"eventLevel":"正向","keywords":"","name":"黄南世纪华联商贸有限公司","digest":"，其中，黄南世纪华联商贸有限公司产品抽检合格"
		events = k.__next__()
		for event in events:
			print(event)
		