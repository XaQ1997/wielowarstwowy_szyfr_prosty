import csv
import json

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
		
		if self.keycodes!=len(data["keycodes"]):
			print("Błąd w standardzie")
			exit(1)
		
		with open(rf"{self.path}\alphabet.csv", newline="") as alphabet:
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
		
		with open(rf"{self.path}\code_covers.csv", newline="") as code_covers:
			filereader=csv.reader(code_covers, delimiter="|")
			next(filereader)
			
			keycodes=[]
			
			for line in filereader:
				layer={"ABBR": line[1]}
				
				if len(line[2])>0:
					layer["keycodes"]=line[2]
					keycodes.append(line[2])
				
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
		
		with open(rf"{self.path}\keyboard_keys.csv", newline="") as keyboard:
			filereader=csv.reader(keyboard, delimiter="|")
			next(filereader)
			
			for line in filereader:
				self.keyboard_codes.append({"char": line[0], "value": line[1]})
		
		if len(self.keyboard_codes)!=len(self.length["keyboard keys"]):
			print("Błąd w standardzie")
			exit(1)
	
	def read(self):
		pass