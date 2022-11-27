class FenceCode:
	def __init__(self, key=2, alphabet="AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"):
		self.key=key
		self.alphabet=alphabet
	
	def encode(self, text):
		tmp=[]
		
		for i in range(self.key):
			tmp.append("")
		
		for i in range(len(text)):
			tmp[i%self.key]+=text[i]
		
		result=""
		
		for i in range(self.key):
			result+=tmp[i]
		
		return result
	
	def decode(self, text):
		if len(text)<self.key-1:
			return text
		
		tmp=[]
		result=""
		
		for i in range(self.key):
			if i*len(text)%self.key<self.key-1:
				tmp.append(text[i*len(text)//self.key: ((i+1)*len(text)//self.key)])
			else:
				tmp.append(text[(i*len(text)//self.key)+1:(i+1)*len(text)//self.key])
			
			if i*len(text)%self.key==self.key-2:
				tmp[i]+=text[((i+1)*len(text)//self.key)]
		
		for i in range(len(text)):
			result+=tmp[i%self.key][i//self.key]
		
		return result
	
	def name(self):
		return f"fence code with key {self.key}"

class ReversedFenceCode(FenceCode):
	def __init__(self, key=2, alphabet="AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"):
		super().__init__(key, alphabet)
	
	def encode(self, text):
		return super().decode(text)
	
	def decode(self, text):
		return super().encode(text)
	
	def name(self):
		return f"reversed fence code with key {self.key}"