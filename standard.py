import csv
import json

from alphabet_code import *
from complex_code import *
from compression_code import *
from conversion_code import *
from fake_letter_code import *
from fence_code import *
from huffman_code import *
from inversion_code import *
from letter_word_code import *
from shuttle_code import *
from trail_code import *

class Standard:
	def __init__(self, name):
		self.name=name
		self.path=rf"standards\{self.name}.scsp"
		self.alphabet=[]
		self.code_covers=[]
		self.keyboard_codes=[]
		
		filereader=""
		
		with open(rf"{self.path}\data.json") as dict:
			filereader=dict.read()
		
		data=json.loads(filereader)
		
		self.encoding=data["encoding"]
		self.length=data["length"]
		self.keycodes=int(self.length["keycodes"])
		self.compression_values=data["compressing"]
		keys=list(data["keycodes"])
		
		for i in range(len(data["keycodes"])):
			keycode=str(data["keycodes"][i])
			keycode=keycode.replace("[", "")
			keycode=keycode.replace("]", "")
			keycode=keycode.replace(",", "")
			keycode=keycode.replace("'", "")
			data["keycodes"][i]=keycode
		
		if self.keycodes!=len(data["keycodes"]):
			print("Błąd w standardzie")
			exit(1)
		
		with open(rf"{self.path}\alphabet.csv", newline="", encoding=self.encoding) as alphabet:
			filereader=csv.reader(alphabet, delimiter="|")
			next(filereader)
			
			for line in filereader:
				letter={"letter": line[1], "LETTER": line[2], "bit value": line[3], "word key": line[4]}
				self.alphabet.append(letter)
			
		if int(self.length["alphabet"])!=len(self.alphabet):
			print("Błąd w standardzie")
			exit(1)
		
		for i in range(len(self.alphabet)):
			if int(self.length["bit value letter"])!=len(self.alphabet[i]["bit value"]):
				print("Błąd w standardzie")
				exit(1)
		
		keycodes=[]
		
		with open(rf"{self.path}\code_covers.csv", newline="", encoding=self.encoding) as code_covers:
			filereader=csv.reader(code_covers, delimiter="|")
			next(filereader)
			
			for line in filereader:
				layer={"ABBR": line[1]}
				
				if len(line[2])>0:
					keycodes.append(line[2])
					
					layer["keycodes"]=keys[len(keycodes)-1]
				
				self.code_covers.append(layer)
		
		if int(self.length["code covers"])!=len(self.code_covers):
			print("Błąd w standardzie")
			exit(1)
		
		if len(keycodes)!=self.keycodes:
			print("Błąd w standardzie")
			exit(1)
		
		for i in range(len(keycodes)):
			if data["keycodes"][i]!=keycodes[i]:
				print("Błąd w standardzie")
				exit(1)
		
		with open(rf"{self.path}\keyboard_keys.csv", newline="", encoding=self.encoding) as keyboard:
			filereader=csv.reader(keyboard, delimiter="|")
			next(filereader)
			
			for line in filereader:
				if line[0]=="ENDL":
					line[0]="\n"
				if line[0]=="SPACE":
					line[0]=" "
				if line[0]=="TAB":
					line[0]="\t"
				if line[0]=="APOSTROPHE":
					line[0]="\'"
				if line[0]=="CITE":
					line[0]="\""
				
				self.keyboard_codes.append({"char": line[0], "value": line[1]})
		
		if len(self.keyboard_codes)!=int(self.length["keyboard keys"]):
			print("Błąd w standardzie")
			exit(1)
	
	def read(self):
		result={"encoding": self.encoding, "alphabet": [], "code covers": []}
		
		alphabet=""
		wordAlphabet={}
		
		for i in range(len(self.alphabet)):
			result["alphabet"].append({"letter": self.alphabet[i]["LETTER"], "word key": self.alphabet[i]["word key"]})
			alphabet+=self.alphabet[i]["LETTER"]
			wordAlphabet[self.alphabet[i]["LETTER"]]=self.alphabet[i]["word key"]
		
		for i in range(len(self.code_covers)):
			layer=None
			
			if self.code_covers[i]["ABBR"]=="BIC":
				layer=BasicInversionCode()
			if self.code_covers[i]["ABBR"]=="DIC":
				layer=DoubleInversionCode()
			if self.code_covers[i]["ABBR"]=="CGIC":
				layer=ConstGroupInversionCode(self.code_covers[i]["keycodes"])
			if self.code_covers[i]["ABBR"]=="WIC":
				layer=WordInversionCode()
			if self.code_covers[i]["ABBR"]=="SIC":
				layer=SentenceInversionCode()
			if self.code_covers[i]["ABBR"]=="RFLC":
				layer=RandomFakeLetterCode(alphabet)
			if self.code_covers[i]["ABBR"]=="AFLC":
				layer=AndFakeLetterCode(alphabet)
			if self.code_covers[i]["ABBR"]=="OFLC":
				layer=OrFakeLetterCode(alphabet)
			if self.code_covers[i]["ABBR"]=="XFLC":
				layer=XorFakeLetterCode(alphabet)
			if self.code_covers[i]["ABBR"]=="RFC":
				layer=ReversedFenceCode(self.code_covers[i]["keycodes"])
			if self.code_covers[i]["ABBR"]=="BSC":
				layer=BasicShuttleCode()
			if self.code_covers[i]["ABBR"]=="OWSC":
				layer=OutWordShuttleCode()
			if self.code_covers[i]["ABBR"]=="IWSC":
				layer=InWordShuttleWord()
			if self.code_covers[i]["ABBR"]=="TC":
				layer=TrailCode(self.code_covers[i]["keycodes"], alphabet)
			if self.code_covers[i]["ABBR"]=="ATC":
				layer=AntiTrailCode(self.code_covers[i]["keycodes"], alphabet)
			if self.code_covers[i]["ABBR"]=="BSTC":
				layer=BasicSynchronousTrailCode(self.code_covers[i]["keycodes"], alphabet)
			if self.code_covers[i]["ABBR"]=="STC":
				layer=SynchronousTrailCode(self.code_covers[i]["keycodes"][0], self.code_covers[i]["keycodes"][1], alphabet)
			if self.code_covers[i]["ABBR"]=="AsTC":
				layer=AsynchronousTrailCode(self.code_covers[i]["keycodes"][0], [self.code_covers[i]["keycodes"][1], self.code_covers[i]["keycodes"][2]], alphabet)
			if self.code_covers[i]["ABBR"]=="LWC":
				layer=LetterWordCode(wordAlphabet)
			if self.code_covers[i]["ABBR"]=="AKC":
				layer=AlphabetKeyCode(self.code_covers[i]["keycodes"], alphabet)
			if self.code_covers[i]["ABBR"]=="AVC":
				layer=AlphabetVectorCode(self.code_covers[i]["keycodes"], alphabet)
			if self.code_covers[i]["ABBR"]=="ABC":
				layer=AtBashCode(alphabet)
			if self.code_covers[i]["ABBR"]=="AtTC":
				layer=AlphabetTableCode(self.code_covers[i]["keycodes"], alphabet)
			if self.code_covers[i]["ABBR"]=="RAC":
				layer=RaiseAlphabetCode(alphabet)
			if self.code_covers[i]["ABBR"]=="RGIC":
				layer=RaisingGroupInversionCode()
			if self.code_covers[i]["ABBR"]=="NLC":
				layer=NumberLetterConversion(alphabet)
			if self.code_covers[i]["ABBR"]=="KC":
				layer=KeyboardCode(self.keyboard_codes)
			if self.code_covers[i]["ABBR"]=="FC":
				layer=FenceCode(self.code_covers[i]["keycodes"], alphabet)
			if self.code_covers[i]["ABBR"]=="CC":
				layer=ConversionCode(self.code_covers[i]["keycodes"])
			if self.code_covers[i]["ABBR"]=="iC":
				layer=ComplexCode(self.code_covers[i]["keycodes"][0], self.code_covers[i]["keycodes"][1], self.code_covers[i]["keycodes"][2])
			if self.code_covers[i]["ABBR"]=="MiC":
				layer=MixedComplexCode(self.code_covers[i]["keycodes"][0], self.code_covers[i]["keycodes"][1])
			if self.code_covers[i]["ABBR"]=="SiC":
				layer=SumComplexCode(self.code_covers[i]["keycodes"][0], self.code_covers[i]["keycodes"][1], self.code_covers[i]["keycodes"][2])
			if self.code_covers[i]["ABBR"]=="MSiC":
				layer=MixedSumComplexCode(self.code_covers[i]["keycodes"][0], self.code_covers[i]["keycodes"][1])
			if self.code_covers[i]["ABBR"]=="HC":
				layer=HuffmanCode()
			if self.code_covers[i]["ABBR"]=="cc":
				layer=CompressionCode(self.code_covers[i]["keycodes"], self.compression_values["onces"], self.compression_values["riffle"], self.compression_values["multiple"])
			
			result["code covers"].append(layer)
		
		return result
	
	def set_keycodes(self, new_keycodes):
		for index in new_keycodes:
			self.keycodes[index]=new_keycodes[index]