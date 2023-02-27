from codec import *
from standard import *

if __name__=="__main__":
	std=Standard("PS_WSP_0")
	
	values=std.read()
	code_covers=values["code covers"]
	encoding=values["encoding"]
	
	covering=13
	
	coder=Coder(code_covers, encoding, covering)
	decoder=Decoder(code_covers, encoding, covering)
	
	coder.run("zrodlo.txt", "wyniki")
	text=decoder.run("wyniki")
	
	print(text)
	
	exit(0)