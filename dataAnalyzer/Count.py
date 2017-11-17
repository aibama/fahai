from LtpService import *
import logging
import loggingSet
from LtpService.ltpService import ltpService
from dataService.dataFactory import fahaiDataFactory

logger = logging.getLogger('root')

def coutTitle():
	contContain = []
	d = fahaiDataFactory()
	data = d.dataAnalyze()
	ltp = ltpService()
	# if data.hasNext():
	# 	next = data.__next__()
	# 	print(next)
	for i in range(10):
			item = data.__next__()
			logger.debug(item['title'])
			logger.debug(ltp.segProvider(item['title']))
			logger.debug(ltp.postAggerProvider(item['title']))
			#contContain.append(ltp.postAggerProvider(next['title']))

if __name__ == "__main__":
	coutTitle()
