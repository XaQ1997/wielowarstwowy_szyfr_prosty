class KeyboardCode:
	def __init__(self, keycode):
		self.keycode=keycode
	
	def encode(self, text):
		result=""
		
		for i in range(len(text)):
			if i!=0:
				result+=" "
			for key in self.keycode:
				if text[i]==key:
					result+=self.keycode[key]
		
		return result
	
	def decode(self, text):
		result=""
		tmp=text.split(" ")
		
		for i in range(len(tmp)):
			for key in self.keycode:
				if tmp[i]==self.keycode[key]:
					result+=key
		
		return result
	
	def name(self):
		return "keyboard code"