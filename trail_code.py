class TrailCode:
	def __init__(self, keyword, alphabet="AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"):
		self.keyword=keyword
		keycode=[]
		
		for i in range(len(keyword)):
			for j in range(len(alphabet)):
				if alphabet[j]==keyword[i]:
					keycode.append(j)
		
		self.keycode=[]
		
		for i in range(len(keyword)):
			self.keycode.append(keyword[i])
		
		for i in range(len(keycode)-1):
			for j in range(len(keycode)-1):
				if keycode[j]>keycode[j+1]:
					tmp=keycode[j]
					keycode[j]=keycode[j+1]
					keycode[j+1]=tmp
					
					tmp=self.keycode[j]
					self.keycode[j]=self.keycode[j+1]
					self.keycode[j+1]=tmp
	
	def encode(self, text):
		tmp=[]
		
		for i in range(len(self.keyword)):
			tmp.append("")
		
		for i in range(len(text)):
			tmp[i%len(self.keyword)]+=text[i]
			
		count=0
		
		for i in range(len(text)%len(self.keyword), len(self.keyword)):
			tmp[i]+="X"
			count+=1
		
		result=""
		
		for i in range(len(self.keycode)):
			for j in range(len(self.keyword)):
				if self.keyword[j]==self.keycode[i]:
					result+=tmp[j]
					
		result = f"{count} \n{result}"
		
		return result
	
	def decode(self, text):
		count = int(text[:text.index("\n")])
		temp=text[count-2:]
		
		tmp=[]
		result=""
		
		for i in range(len(self.keyword)):
			for j in range(len(self.keycode)):
				if self.keycode[j]==self.keyword[i]:
					tmp.append(temp[j*len(temp)//len(self.keyword): (j+1)*len(temp)//len(self.keyword)])
		
		for i in range(len(temp)-count):
			result+=tmp[i%len(self.keyword)][i//len(self.keyword)]
		
		return result
	
	def name(self):
		return f"trail code with keyword {self.keyword}"

class AntiTrailCode:
	def __init__(self, keyword, alphabet="AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"):
		self.keyword = keyword
		keycode = []
		
		for i in range(len(keyword)):
			for j in range(len(alphabet)):
				if alphabet[j] == keyword[i]:
					keycode.append(j)
		
		self.keycode = []
		
		for i in range(len(keyword)):
			self.keycode.append(keyword[i])
		
		for i in range(len(keycode) - 1):
			for j in range(len(keycode) - 1):
				if keycode[j] < keycode[j + 1]:
					tmp = keycode[j]
					keycode[j] = keycode[j + 1]
					keycode[j + 1] = tmp
					
					tmp = self.keycode[j]
					self.keycode[j] = self.keycode[j + 1]
					self.keycode[j + 1] = tmp
	
	def encode(self, text):
		tmp = []
		
		for i in range(len(self.keyword)):
			tmp.append("")
		
		for i in range(len(text)):
			tmp[i % len(self.keyword)] += text[i]
		
		count = 0
		
		for i in range(len(text) % len(self.keyword), len(self.keyword)):
			tmp[i] += "X"
			count += 1
		
		result = ""
		
		for i in range(len(self.keycode)):
			for j in range(len(self.keyword)):
				if self.keyword[j] == self.keycode[i]:
					result += tmp[j]
		
		result=f"{count} \n{result}"
		
		return result
	
	def decode(self, text):
		count=int(text[:text.index("\n")])
		temp=text[count-2:]
		
		tmp = []
		result = ""
		
		for i in range(len(self.keyword)):
			for j in range(len(self.keycode)):
				if self.keycode[j] == self.keyword[i]:
					tmp.append(temp[j * len(temp) // len(self.keyword): (j + 1) * len(temp) // len(self.keyword)])
		
		for i in range(len(temp) - count):
			result += tmp[i % len(self.keyword)][i // len(self.keyword)]
		
		return result
	
	def name(self):
		return f"anti trail code with keyword {self.keyword}"



class SynchronousTrailCode:
	def __init__(self, keyword, keycode, alphabet="AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"):
		self.keyword = keyword
		keyc = []
		self.keycode=keycode
		
		for i in range(len(keyword)):
			for j in range(len(alphabet)):
				if alphabet[j] == keyword[i]:
					keyc.append(j)
		
		self.keyc = []
		
		for i in range(len(keyword)):
			self.keyc.append(keyword[i])
		
		for i in range(len(keyc) - 1):
			for j in range(len(keyc) - 1):
				if keyc[j] > keyc[j + 1]:
					tmp = keyc[j]
					keyc[j] = keyc[j + 1]
					keyc[j + 1] = tmp
					
					tmp = self.keyc[j]
					self.keyc[j] = self.keyc[j + 1]
					self.keyc[j + 1] = tmp
	
	def encode(self, text):
		tmp = []
		
		for i in range(len(self.keyword)):
			tmp.append("")
		
		for i in range(len(text)):
			length=i//len(self.keyword)
			rest=i%len(self.keyword)
			
			if length%(2*self.keycode)>=self.keycode:
				tmp[len(self.keyword)-rest-1] += text[i]
			else:
				tmp[rest]+=text[i]
		
		count = 0
		
		for i in range(len(text) % len(self.keyword), len(self.keyword)):
			length=i//len(self.keyword)
			if length%(2*self.keycode)>=self.keycode:
				tmp[len(self.keyword)-i-1] += "X"
			else:
				tmp[i]+="X"
			count += 1
		
		result = ""
		
		for i in range(len(self.keyc)):
			for j in range(len(self.keyword)):
				if self.keyword[j] == self.keyc[i]:
					result += tmp[j]
		
		result=f"{count} \n{result}"
		
		return result
	
	def decode(self, text):
		count=int(text[:text.index("\n")])
		temp=text[count-2:]
		
		tmp = []
		result = ""
		
		for i in range(len(self.keyword)):
			for j in range(len(self.keyc)):
				if self.keyc[j] == self.keyword[i]:
					tmp.append(temp[j * len(temp) // len(self.keyword): (j + 1) * len(temp) // len(self.keyword)])
		
		for i in range(len(temp) - count):
			length=i//len(self.keyword)
			rest=i%len(self.keyword)
			if length%(2*self.keycode)<self.keycode:
				result += tmp[rest][length]
			else:
				result+=tmp[len(self.keyword)-rest-1][length]
		
		return result
	
	def name(self):
		return f"{self.keycode}-synchronous trail code with keyword {self.keyword}"

class BasicSynchronousTrailCode(SynchronousTrailCode):
	def __init__(self, keyword, alphabet="AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"):
		super().__init__(keyword, 1, alphabet)
	
	def name(self):
		return f"basic synchronous trail code with keyword {self.keyword}"

class AsynchronousTrailCode:
	def __init__(self, keyword, direction, alphabet="AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"):
		self.keyword = keyword
		keycode = []
		self.direction=direction
		self.length=self.direction[0]+self.direction[1]
		
		for i in range(len(keyword)):
			for j in range(len(alphabet)):
				if alphabet[j] == keyword[i]:
					keycode.append(j)
		
		self.keycode = []
		
		for i in range(len(keyword)):
			self.keycode.append(keyword[i])
		
		for i in range(len(keycode) - 1):
			for j in range(len(keycode) - 1):
				if keycode[j] > keycode[j + 1]:
					tmp = keycode[j]
					keycode[j] = keycode[j + 1]
					keycode[j + 1] = tmp
					
					tmp = self.keycode[j]
					self.keycode[j] = self.keycode[j + 1]
					self.keycode[j + 1] = tmp
	
	def encode(self, text):
		tmp = []
		
		for i in range(len(self.keyword)):
			tmp.append("")
		
		for i in range(len(text)):
			length = i // len(self.keyword)
			rest = i % len(self.keyword)
			
			if length % self.length >= self.direction[0]:
				tmp[len(self.keyword) - rest - 1] += text[i]
			else:
				tmp[rest] += text[i]
		
		count = 0
		
		for i in range(len(text) % len(self.keyword), len(self.keyword)):
			length = i // len(self.keyword)
			if length % self.length >= self.direction[0]:
				tmp[len(self.keyword) - i - 1] += "X"
			else:
				tmp[i] += "X"
			count += 1
		
		result = ""
		
		for i in range(len(self.keycode)):
			for j in range(len(self.keyword)):
				if self.keyword[j] == self.keycode[i]:
					result += tmp[j]
		
		result=f"{count} \n{result}"
		
		return result
	
	def decode(self, text):
		count=int(text[:text.index("\n")])
		temp=text[count-2:]
		
		tmp = []
		result = ""
		
		for i in range(len(self.keyword)):
			for j in range(len(self.keycode)):
				if self.keycode[j] == self.keyword[i]:
					tmp.append(temp[j * len(temp) // len(self.keyword): (j + 1) * len(temp) // len(self.keyword)])
		
		for i in range(len(temp) - count):
			length = i // len(self.keyword)
			rest = i % len(self.keyword)
			if length % self.length < self.direction[0]:
				result += tmp[rest][length]
			else:
				result += tmp[len(self.keyword) - rest - 1][length]
		
		return result
	
	def name(self):
		return f"<{self.direction[0]}; {self.direction[1]}>-asynchronous trail code with keyword {self.keyword}"