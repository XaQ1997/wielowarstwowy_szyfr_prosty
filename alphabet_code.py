from inversion_code import *

class AlphabetKeyCode:
	def __init__(self, keyword, alphabet="AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"):
		self.key_alphabet=keyword
		self.alphabet=alphabet
		self.keyword=keyword
		
		for i in range(len(self.alphabet)):
			for j in range(len(self.key_alphabet)):
				if self.alphabet[i]==self.key_alphabet[j]:
					break
				if j==len(self.key_alphabet)-1:
					self.key_alphabet+=self.alphabet[i]

	def encode(self, text):
		result=""
		
		for i in range(len(text)):
			for j in range(len(self.alphabet)):
				if text[i]==self.alphabet[j]:
					result+=self.key_alphabet[j]
					break
				
				if j==len(self.alphabet)-1:
					result+=text[i]
		
		return result
	
	def decode(self, text):
		result=""
		
		for i in range(len(text)):
			for j in range(len(self.key_alphabet)):
				if text[i]==self.key_alphabet[j]:
					result+=self.alphabet[j]
					break
				
				if j==len(self.alphabet)-1:
					result+=text[i]
		
		return result

	def name(self):
		return f"code with alphabet key {self.keyword}"

class AlphabetVectorCode:
	def __init__(self, key, alphabet="AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"):
		self.key=key
		self.alphabet=alphabet
	
	def encode(self, text):
		result=""
		
		for i in range(len(text)):
			for j in range(len(self.alphabet)):
				if text[i]==self.alphabet[j]:
					result+=self.alphabet[(j+self.key)%len(self.alphabet)]
					break
				
				if j==len(self.alphabet)-1:
					result+=text[i]
		
		return result
	
	def decode(self, text):
		result=""
		
		for i in range(len(text)):
			for j in range(len(self.alphabet)):
				if text[i]==self.alphabet[j]:
					result+=self.alphabet[(j-self.key)%len(self.alphabet)]
					break
				
				if j==len(self.alphabet)-1:
					result+=text[i]
		
		return result
	
	def name(self):
		return f"alphabet vector code with key {self.key}"

class AtBashCode(AlphabetKeyCode):
	def __init__(self, alphabet="AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"):
		keyword=BasicInversionCode().encode(alphabet)
		super().__init__(keyword, alphabet)
	
	def name(self):
		return "at bash code"

class AlphabetTableCode(AlphabetKeyCode):
	def __init__(self, key, alphabet="AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"):
		keyword=""
		self.key=key
		
		for i in range(len(alphabet)):
			index=i
			length=i%key
			sublen=i//key
			
			if 2*length<key:
				index+=length
			else:
				index-=key-length
			
			if 2*sublen<len(alphabet)//key:
				index+=key*sublen
			else:
				index-=len(alphabet)-key*sublen
			
			index%=len(alphabet)
			
			keyword+=alphabet[index]
		
		super().__init__(keyword, alphabet)
	
	def name(self):
		return f"alphabet table code with key {self.key}"

class RaiseAlphabetCode:
	def __init__(self, alphabet="AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"):
		self.alphabet=alphabet
	
	def encode(self, text):
		move=0
		index=0
		result=""
		
		for i in range(len(text)):
			for j in range(len(self.alphabet)):
				if text[i]==self.alphabet[j]:
					result+=self.alphabet[(j+index)%len(self.alphabet)]
					break
				
				if len(self.alphabet)==j+1:
					result+=text[i]
					index-=move
			
			if index%len(self.alphabet)==0:
				move+=1
			
			index+=move
		
		return result
	
	def decode(self, text):
		move=0
		index=0
		result=""
		
		for i in range(len(text)):
			for j in range(len(self.alphabet)):
				if text[i]==self.alphabet[j]:
					result+=self.alphabet[(j-index)%len(self.alphabet)]
					break
				
				if len(self.alphabet)==j+1:
					result+=text[i]
					index-=move
			
			if index%len(self.alphabet)==0:
				move+=1
			
			index+=move
		
		return result
	
	def name(self):
		return "raise alphabet code"