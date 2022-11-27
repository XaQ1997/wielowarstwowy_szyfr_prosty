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