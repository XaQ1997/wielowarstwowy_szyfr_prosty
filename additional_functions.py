from math import *
from sys import *
setrecursionlimit(10**6)

def division(value, divide=1):
	return (value//divide, value%divide)

class Convert:
	def __init__(self, system):
		self.system=system
	
	def count_to(self, n, number=""):
		if n==0:
			return number[::-1]
		
		number+=str(n%self.system)
		return self.count_to(n//self.system, number)
	
	def count_from(self, number):
		tmp=0
		
		for i in range(len(number)):
			tmp+=int(number[i])*self.system**(len(number)-i-1)
		
		return str(tmp)

class Complex:
	def __init__(self, amplitude, phase):
		self.real=amplitude*round(cos(phase), 6)
		self.imagine=amplitude*round(sin(phase), 6)
		
		if self.real==int(self.real):
			self.real=int(self.real)
		if self.imagine==int(self.imagine):
			self.imagine=int(self.imagine)
	
	def write(self, tech):
		if self.real!=0.0:
			if self.imagine>0.0:
				if tech=="math":
					if self.imagine==1.0:
						return f"({self.real}+i)"
					return f"({self.real}+{self.imagine}i)"
				if tech=="tech":
					if self.imagine==1.0:
						return f"({self.real}+j)"
					return f"({self.real}+{self.imagine}j)"
			elif self.imagine==0.0:
				return f"{self.real}"
			else:
				if tech=="math":
					if self.imagine == -1.0:
						return f"({self.real}-i)"
					return f"({self.real}{self.imagine}i)"
				if tech=="tech":
					if self.imagine == -1.0:
						return f"({self.real}-j)"
					return f"({self.real}{self.imagine}j)"
		else:
			if self.imagine==0.0:
				return "0"
			if tech=="math":
				if abs(self.imagine)==1.0:
					return "i"
				return f"{self.imagine}i"
			if tech=="tech":
				if abs(self.imagine)==1.0:
					return "j"
				return f"{self.imagine}j"
	
	def sum_write(self, tech, real=0.0, imagine=0.0):
		if self.real+real!=0.0:
			if self.imagine+imagine>0.0:
				if tech=="math":
					if self.imagine+imagine==1.0:
						return f"({self.real+real}+i)"
					return f"({self.real+real}+{self.imagine+imagine}i)"
				if tech=="tech":
					if self.imagine+imagine==1.0:
						return f"({self.real+real}+j)"
					return f"({self.real+real}+{self.imagine+imagine}j)"
			elif self.imagine+imagine==0.0:
				return f"{self.real+real}"
			else:
				if tech=="math":
					if self.imagine+imagine == -1.0:
						return f"({self.real+real}-i)"
					return f"({self.real+real}{self.imagine+imagine}i)"
				if tech=="tech":
					if self.imagine+imagine == -1.0:
						return f"({self.real+real}-j)"
					return f"({self.real+real}{self.imagine+imagine}j)"
		else:
			if self.imagine+imagine==0.0:
				return "0"
			if tech=="math":
				if abs(self.imagine+imagine)==1.0:
					return "i"
				return f"{self.imagine+imagine}i"
			if tech=="tech":
				if abs(self.imagine+imagine)==1.0:
					return "j"
				return f"{self.imagine+imagine}j"