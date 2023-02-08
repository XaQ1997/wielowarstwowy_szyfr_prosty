from codec import *
from standard import *

if __name__=="__main__":
	std=Standard("PS_WSP_0")
	
	coder=Coder(code_covers, 1)
	decoder=Decoder(code_covers, 1)
	
	coder.run("zrodlo.txt", "wyniki")
	text=decoder.run("wyniki")
	
	print(text)