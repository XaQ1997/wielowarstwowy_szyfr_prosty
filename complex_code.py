from additional_functions import *

from math import *
from random import *

class ComplexCode:
	def __init__(self, tech, start_amplitude=1, start_phase=0):
		self.amplitude=start_amplitude
		self.phase=(start_phase*(2*pi)/360.0)
		self.tech=tech
	
	def encode(self, text):
		tmp=text.split(" ")
		result=""
		
		for i in range(len(tmp)):
			count=0
			
			for j in range(len(tmp[i])):
				value=int(tmp[i][j])
				complex=Complex(value*((self.amplitude+i)/(2**j)), self.phase+(count*pi/2))
				
				if value!=0:
					count+=1
				
				if j!=0:
					result+=" "
				
				result+=complex.write(self.tech)
			
			if i<len(tmp)-1:
				result+="\t"
		
		return result
	
	def decode(self, text):
		t=str.replace(text, "(", "")
		r=str.replace(t, ")", "")
		
		tmp=r.split("\t")
		temp=[]
		result=""
		
		for i in range(len(tmp)):
			temp.append(tmp[i].split(" "))
		
		for i in range(len(temp)):
			for j in range(len(temp[i])):
				if temp[i][j]=="0":
					result+="0"
				else:
					result+="1"
			
			if i<len(temp)-1:
				result+=" "
		
		return result
	
	def name(self):
		return "complex code"

class MixedComplexCode:
	def __init__(self, start_amplitude=1, start_phase=0):
		self.amplitude=start_amplitude
		self.phase=start_phase
		
	def encode(self, text):
		tmp=text.split(" ")
		result=""
		
		for i in range(len(tmp)):
			count=0
			
			for j in range(len(tmp[i])):
				value=int(tmp[i][j])
				complex=Complex(value*((self.amplitude+i)/(2**j)), self.phase+(count*pi/2))
				
				if value!=0:
					count+=1
				
				if j!=0:
					result+=" "
			
				tech=["math", "tech"]
			
				rnd=randint(0, 1)
			
				result+=complex.write(tech[rnd])
		
			if i<len(tmp)-1:
				result+="\t"
		
		return result
	
	def decode(self, text):
		t=str.replace(text, "(", "")
		r=str.replace(t, ")", "")
		
		tmp=r.split("\t")
		temp=[]
		result=""
		
		for i in range(len(tmp)):
			temp.append(tmp[i].split(" "))
		
		for i in range(len(temp)):
			for j in range(len(temp[i])):
				if temp[i][j]=="0":
					result+="0"
				else:
					result+="1"
			
			if i<len(temp)-1:
				result+=" "
		
		return result
	
	def name(self):
		return "mixed complex code"

class SumComplexCode:
	def __init__(self, tech, start_amplitude=1, start_phase=0):
		self.amplitude=start_amplitude
		self.phase=(start_phase*(2*pi)/360.0)
		self.tech=tech
	
	def encode(self, text):
		tmp=text.split(" ")
		result=""
		sum=[0, 0]
		
		for i in range(len(tmp)):
			count=0
			
			for j in range(len(tmp[i])):
				value=int(tmp[i][j])
				complex=Complex(value*((self.amplitude+i)/(2**j)), self.phase+(count*pi/2))
				
				if value!=0:
					count+=1
				
				if j!=0:
					result+=" "
				
				result+=complex.sum_write(self.tech, sum[0], sum[1])
				
				sum[0]+=complex.real
				sum[1]+=complex.imagine
			
			if i<len(tmp)-1:
				result+="\t"
		
		return result
	
	def decode(self, text):
		t=str.replace(text, "(", "")
		r=str.replace(t, ")", "")
		
		tmp=r.split("\t")
		temp=[]
		result=""
		
		for i in range(len(tmp)):
			temp.append(tmp[i].split(" "))
		
		for i in range(len(temp)):
			for j in range(len(temp[i])):
				if j!=0:
					if temp[i][j]==temp[i][j-1]:
						result+="0"
					else:
						result+="1"
				else:
					if temp[i][j]==temp[i-1][len(temp[i-1])-1] or i==0:
						result+="0"
					else:
						result+="1"
			
			if i<len(temp)-1:
				result+=" "
	
		return result
	
	def name(self):
		return "sum complex code"

class MixedSumComplexCode:
	def __init__(self, start_amplitude=1, start_phase=0):
		self.amplitude = start_amplitude
		self.phase = (start_phase * (2 * pi) / 360.0)
	
	def encode(self, text):
		tmp = text.split(" ")
		result = ""
		sum = [0, 0]
		
		for i in range(len(tmp)):
			count = 0
			
			for j in range(len(tmp[i])):
				value = int(tmp[i][j])
				complex = Complex(value * ((self.amplitude + i) / (2 ** j)), self.phase + (count * pi / 2))
				
				if value != 0:
					count += 1
				
				if j != 0:
					result += " "
				
				tech=["math", "tech"]
				rnd=randint(0, 1)
				
				result += complex.sum_write(tech[rnd], sum[0], sum[1])
				
				sum[0] += complex.real
				sum[1] += complex.imagine
			
			if i < len(tmp) - 1:
				result += "\t"
		
		return result
	
	def decode(self, text):
		t = str.replace(text, "(", "")
		r = str.replace(t, ")", "")
		
		tmp = r.split("\t")
		temp = []
		result = ""
		
		for i in range(len(tmp)):
			temp.append(tmp[i].split(" "))
		
		for i in range(len(temp)):
			for j in range(len(temp[i])):
				if j != 0:
					if temp[i][j] == temp[i][j - 1]:
						result += "0"
					else:
						result += "1"
				else:
					if temp[i][j] == temp[i - 1][len(temp[i - 1]) - 1] or i == 0:
						result += "0"
					else:
						result += "1"
			
			if i < len(temp) - 1:
				result += " "
		
		return result
	
	def name(self):
		return "mixed sum complex code"