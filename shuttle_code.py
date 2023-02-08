class BasicShuttleCode:
	def __init__(self):
		pass
	
	def encode(self, text):
		length=len(text)-1
		result=""
		
		if len(text)%2==1:
			length-=1
		
		for i in range(length, 0, -2):
			result+=text[i]
		
		for i in range(0, len(text), 2):
			result+=text[i]
		
		return result
	
	def decode(self, text):
		if text=="":
			return text
		
		result=""
		
		half=len(text)//2
		
		for i in range(half+1):
			result+=text[half-i]
			
			if half+i<len(text) and i!=0:
				result+=text[half+i]
		
		return result
	
	def name(self):
		return "basic shuttle code"

class OutWordShuttleCode:
	def __init__(self):
		pass
	
	def encode(self, text):
		tmp=text.split(" ")
		
		result=[]
		
		length=len(tmp)-1
		
		if len(tmp)%2==1:
			length-=1
		
		for i in range(length, 0, -2):
			result.append(tmp[i])
		
		for i in range(0, len(tmp), 2):
			result.append(tmp[i])
		
		return str.join(" ", result)
	
	def decode(self, text):
		tmp=text.split(" ")
		result=[]
		
		half=len(tmp)//2
		
		for i in range(half+1):
			result.append(tmp[half-i])
			
			if half+i<len(tmp) and i!=0:
				result.append(tmp[half+i])
		
		return str.join(" ", result)
	
	def name(self):
		return "out-word shuttle code"

class InWordShuttleWord:
	def __init__(self):
		pass
	
	def encode(self, text):
		tmp=text.split(" ")
		result=[]
		
		for i in range(len(tmp)):
			result.append("")
			length = len(tmp[i]) - 1
			
			if len(tmp[i]) % 2 == 1:
				length -= 1
			
			for j in range(length, 0, -2):
				result[i] += tmp[i][j]
			
			for j in range(0, len(tmp[i]), 2):
				result[i] += tmp[i][j]
		
		return str.join(" ", result)
	
	def decode(self, text):
		if text=="":
			return text
		
		tmp=text.split(" ")
		result=[]
		
		for i in range(len(tmp)):
			result.append("")
			half=len(tmp[i])//2
			
			for j in range(half):
				result[i]+=tmp[i][half-j]
				
				if half+j<len(tmp[i]) and j!=0:
					result[i]+=tmp[i][half+j]
		
		return str.join(" ", result)
	def name(self):
		return "basic in-word shuttle code"