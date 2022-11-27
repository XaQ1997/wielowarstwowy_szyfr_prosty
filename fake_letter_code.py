from random import *

class FakeLetterCode:
	def __init__(self, way, alphabet='AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ'):
		self.way=way
		self.alphabet=alphabet
	
	def encode(self, text):
		result=""
		for i in range(len(text)):
			result+=text[i]
			if i+1<len(text) and i%2==0:
				if self.way=="random":
					result+=self.alphabet[randint(0, len(self.alphabet)-1)]
				if self.way=="and":
					is_found=False
					for j in range(len(self.alphabet)):
						if text[i]==self.alphabet[j]:
							for k in range(len(self.alphabet)):
								if text[i+1]==self.alphabet[k]:
									result+=self.alphabet[j&k]
									is_found=True
						
						if j+1==len(self.alphabet) and is_found==False:
							result+=self.alphabet[randint(0, len(self.alphabet)-1)]
		
				if self.way=="or":
					is_found = False
					for j in range(len(self.alphabet)):
						if text[i] == self.alphabet[j]:
							for k in range(len(self.alphabet)):
								if text[i + 1] == self.alphabet[k]:
									tmp=j|k
									if tmp>=len(self.alphabet):
										tmp-=len(self.alphabet)
									
									result+=self.alphabet[tmp]
									
									is_found = True
						
						if j + 1 == len(self.alphabet) and is_found == False:
							result += self.alphabet[randint(0, len(self.alphabet) - 1)]
				
				if self.way=="xor":
					is_found = False
					for j in range(len(self.alphabet)):
						if text[i] == self.alphabet[j]:
							for k in range(len(self.alphabet)):
								if text[i + 1] == self.alphabet[k]:
									tmp=j^k
									if tmp>=len(self.alphabet):
										tmp-=len(self.alphabet)
									
									result+=self.alphabet[tmp]
									
									is_found = True
						
						if j + 1 == len(self.alphabet) and is_found == False:
							result += self.alphabet[randint(0, len(self.alphabet) - 1)]
		
		return result
	
	def decode(self, text):
		result=""
		
		for i in range(len(text)):
			if i%3!=1:
				result+=text[i]
		
		return result
	
class RandomFakeLetterCode(FakeLetterCode):
	def __init__(self, alphabet='AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ'):
		super().__init__("random", alphabet)
	
	def name(self):
		return "random fake letter code"

class AndFakeLetterCode(FakeLetterCode):
	def __init__(self, alphabet='AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ'):
		super().__init__("and", alphabet)
	
	def name(self):
		return "and fake letter code"

class OrFakeLetterCode(FakeLetterCode):
	def __init__(self, alphabet='AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ'):
		super().__init__("or", alphabet)
	
	def name(self):
		return "or fake letter code"

class XorFakeLetterCode(FakeLetterCode):
	def __init__(self, alphabet='AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻż'):
		super().__init__("xor", alphabet)
	
	def name(self):
		return "xor fake letter code"