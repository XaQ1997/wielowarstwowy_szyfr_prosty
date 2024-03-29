class BasicInversionCode:
	def __init__(self):
		pass
	
	def encode(self, text):
		return text[::-1]
	
	def decode(self, text):
		return self.encode(text)
	
	def name(self):
		return "basic inversion code"

class ConstGroupInversionCode:
	def __init__(self, key):
		self.keycode=key
	
	def encode(self, text):
		tmp=[]
		rest=len(text)%self.keycode
		
		for i in range(len(text)//self.keycode):
			tmp.append(text[i*self.keycode:(i+1)*self.keycode][::-1])
		
		tmp.append((text[len(text)-rest:len(text)])[::-1])
		
		return str.join("", tmp)
	
	def decode(self, text):
		return self.encode(text)
	
	def name(self):
		return f"group inversion code with key {self.keycode}"

class DoubleInversionCode(ConstGroupInversionCode):
	def __init__(self):
		self.keycode=2
		super().__init__(self.keycode)
	
	def name(self):
		return "double inversion code"

class WordInversionCode:
	def __init__(self):
		pass
	
	def encode(self, text):
		tmp=text.split(" ")
		temp=[]
		
		for i in range(len(tmp)):
			temp.append(tmp[i][::-1])
		
		return str.join(" ", temp)
	
	def decode(self, text):
		return self.encode(text)
	
	def name(self):
		return "word inversion code"

class SentenceInversionCode:
	def __init__(self):
		pass
	
	def encode(self, text):
		operators=[]
		
		for i in range(len(text)):
			if text[i]==".":
				operators.append(".")
			if text[i]=="!":
				operators.append("!")
			if text[i]=="?":
				operators.append("?")
			if text[i]=="\n":
				operators.append("\n")
		
		tmp=text.replace("!", ".")
		tmp=tmp.replace("?", ".")
		tmp=tmp.replace("\n", ".")
		
		tmp=tmp.split(".")
		
		temp=[]
		
		for i in range(len(tmp)):
			temp.append(tmp[i][::-1])
		
		result=""
		
		for i in range(len(temp)):
			result+=temp[i]
			
			if i+1<len(temp):
				result+=operators[i]
		
		return result
	
	def decode(self, text):
		return self.encode(text)
	
	def name(self):
		return "sentence inversion code"

class RaisingGroupInversionCode:
	def __init__(self):
		pass
	
	def encode(self, text):
		keycode=2
		tmp = []
		place = 0
		
		while place <= len(text):
			tmp.append((text[place:place + keycode:])[::-1])
			
			place += keycode
			keycode+=1
		
		return str.join("", tmp)
	
	def decode(self, text):
		return self.encode(text)
	
	def name(self):
		return "raising group inversion code"