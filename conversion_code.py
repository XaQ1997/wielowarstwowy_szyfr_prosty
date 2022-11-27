from additional_functions import *

class NumberLetterConversion:
	def __init__(self, alphabet="AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"):
		self.alphabet=alphabet
	
	def encode(self, text):
		result=""
		tmp=""
		
		for i in range(len(text)):
			if text[i].isdigit()==True:
				tmp+=text[i]
			else:
				if tmp=="":
					result+=text[i]
				else:
					v=int(tmp)
					value, rest=division(v, len(self.alphabet))
					res=self.alphabet[rest]
					
					while value>=1:
						value, rest=division(value, len(self.alphabet))
						res+=self.alphabet[rest]
						
					result+=f"[{res[::-1]}] "
					
					tmp=""
		
		return result
	
	def decode(self, text):
		is_number=False
		result=""
		tmp=""
		
		for i in range(len(text)):
			if is_number==True:
				if text[i]!="]":
					tmp+=text[i]
			if is_number==False:
				if text[i]!="[":
					result+=text[i]
			
			if text[i]=="[":
				is_number=True
			
			if text[i]=="]":
				is_number=False
				
				number=0
				
				for j in range(len(tmp)):
					for k in range(len(self.alphabet)):
						if tmp[j]==self.alphabet[k]:
							number+=k*len(self.alphabet)**(len(tmp)-j-1)
				
				result+=str(number)
				tmp=""
		
		return result

class ConversionCode:
	def __init__(self, system):
		self.system=system
	
	def encode(self, text):
		tmp=text.split(" ")
		result=""
		
		for i in range(len(tmp)):
			if i!=0:
				result+=" "
			
			is_zero=True
			
			for j in range(len(tmp[i])):
				if int(tmp[i][j])!=0:
					is_zero=False
					
				if is_zero==True:
					result+=tmp[i][j]
			
			result+=Convert(self.system).count_to(int(tmp[i]))
		
		return result
	
	def decode(self, text):
		tmp = text.split(" ")
		result = ""
		
		for i in range(len(tmp)):
			if i != 0:
				result += " "
			
			is_zero=True
			zeros=0
			
			for j in range(len(tmp[i])):
				if int(tmp[i][j])!=0:
					is_zero=False
					
				if is_zero==True:
					result+=tmp[i][j]
					zeros+=1
			
			if is_zero==False:
				if zeros!=0:
					result+=Convert(self.system).count_from(tmp[i][zeros-1:len(tmp[i])])
				else:
					result+=Convert(self.system).count_from(tmp[i])
		
		return result
	
	def name(self):
		return f"conversion code with system {self.system}"