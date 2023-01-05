class HuffmanCode:
	def __init__(self):
		pass
	
	def encode(self, text):
		if text=="":
			return text
		
		tmp=text.split(" ")
		dictio={}
		
		for i in range(len(tmp)):
			if dictio.get(tmp[i])==None:
				dictio[tmp[i]]=0
			
			dictio[tmp[i]]+=1
		
		temp=[]
		
		for key in dictio:
			is_exist=False
			
			for i in range(len(temp)):
				if dictio[key]>dictio[temp[i]]:
					t=temp[i]
					temp[i]=key
					is_exist=True
					
					for j in range(i+1, len(temp)):
						if j<len(temp)-1:
							temporary=temp[j]
							temp[j]=t
							t=temporary
						else:
							temp.append(t)
					break
					
				if i==len(temp)-1:
					temp.append(key)
					is_exist=True
			
			if is_exist==False:
				temp.append(key)
		
		res=""
		dictio={}
		
		for i in range(len(temp)):
			if i==0:
				res="0"
			elif i<len(temp)-1:
				res="1"+res
			else:
				res=""
				for _ in range(len(temp)-1):
					res+="1"
			
			dictio[temp[i]]=res
		
		result="{ \n"
		
		for key in dictio:
			result+=f"\t\"{key}\": {dictio[key]}\n"
		
		result+="} \n"
		
		for i in range(len(tmp)):
			if i!=0:
				result+=" "
			
			result+=f"{dictio[tmp[i]]}"
		
		return result
	
	def decode(self, text):
		if text=="":
			return text
		
		tmp=text.split("\n")
		
		info=tmp[len(tmp)-1].split(" ")
		
		dictio={}
		
		for i in range(1, len(tmp)-2):
			temp=tmp[i].split(": ")
			
			dictio[temp[1]]=temp[0][2:len(temp[0])-1]
		
		result=""
		
		for i in range(len(info)):
			if i!=0:
				result+=" "
			
			result+=dictio[info[i]]
		
		return result
	
	def name(self):
		return "Huffman code"