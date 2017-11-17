import sys, os

ROOTDIR = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path = [os.path.join(ROOTDIR, "lib")] + sys.path

# Set your own model path
MODELDIR=os.path.join(ROOTDIR, "..\ltp_data")

from pyltp import SentenceSplitter, Segmentor, Postagger, Parser, NamedEntityRecognizer, SementicRoleLabeller

class ltpService():
	#划分 供应器
	#like 酒类	中	抽检	葡萄酒	17	批次	
	words = None
	postags = None
	parser = None
	role = None


	"""
	用反射去重构调用；ORM
	因为self.words = none
	postags = none
	parser = none
	没有；导致role调用不成功
	"""
	def segProvider(self,sen):
		sentence = SentenceSplitter.split(sen)[0]
		segmentor = Segmentor()
		segmentor.load(os.path.join(MODELDIR, "cws.model"))
		self.words = segmentor.segment(sentence)
		return ("\t".join(self.words))
	#标注 供应器
	#like n	nd	v	n	m	q	wp
	def postAggerProvider(self,sen):
		if self.words == None:
			self.segProvider(sen)
		postagger = Postagger()
		postagger.load(os.path.join(MODELDIR, "pos.model"))
		self.postags = postagger.postag(self.words)
		return ("\t".join(self.postags))
	#剖析 供应器
	#like 2:ATT	4:ATT	4:ATT	6:ATT	6:ATT	0:HED	6:WP
	def parserProvider(self,sen):
		if self.words == None:
			self.segProvider(sen)
		if self.postags == None:
			self.postAggerProvider(sen)
		parser = Parser()
		parser.load(os.path.join(MODELDIR, "parser.model"))
		self.parser = parser.parse(self.words, self.postags)
		return self.parser
	#SRL 供应器
	#like 3 MNR:(0,1)ADV:(2,2)
	def srlProvider(self,sen):
		if self.words == None:
			self.segProvider(sen)
		if self.postags == None:
			self.postAggerProvider(sen)
		if self.parser == None:
			self.parserProvider(sen)	
		recognizer = NamedEntityRecognizer()
		recognizer.load(os.path.join(MODELDIR, "ner.model"))
		netags = recognizer.recognize(self.words, self.postags)
		labeller = SementicRoleLabeller()
		labeller.load(os.path.join(MODELDIR, "srl/"))
		self.role = labeller.label(self.words, self.postags, netags, self.parser)
		return self.role

if __name__ == "__main__":
	strtest = r"马鞍山市食药监局抽检4类食品29批次样品 全部合格"
	ltp = ltpService()
	print(MODELDIR)
	print(ltp.segProvider(strtest))