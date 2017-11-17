import re
import json
import demjson
file_dir = r"C:\Users\Administrator\PycharmProjects\ltptest2\DATA\DATA_T.txt"

def fileread():
	fin = open(file_dir, 'r',encoding='UTF-8')
	line = fin.read()
	return line
'''
#生成器
#对L进行json的decode
#因为i不带{}会报错；以后可以重构
#l default type = list
'''
def listIter(l):
	for i in l:
		wrap = '{'+i+'}'
		#yield demjson.decode(wrap)
		yield wrap

#i = demjson.decode('{'+findjson[2]+'}')
class fahaiDataFactory():
	"""
	#返回一个item 给项目用
	#带异常处理
	"""
	def dataAnalyze(self):
		pattern = r'\{(.+?)\}'
		content = repr(fileread())
		regex = re.compile(pattern)
		findjson = regex.findall(content)
		#对list循环加｛｝不然转dict会报错
		for i in findjson:
			yield eval('{'+i+'}')

if __name__ == "__main__":
	d = fahaiDataFactory()
	data = d.dataAnalyze()
	dd = data.__next__()
	print(type(dd))