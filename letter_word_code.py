from keyboard_code import *

class LetterWordCode(KeyboardCode):
	def __init__(self, keycode):
		super().__init__(keycode)
		
		self.keycode[" "]="\t"
		self.keycode["\n"]="\n"
		self.keycode["\t"]="\n\t"
		self.keycode["\""]="\""
		self.keycode["."]="."
		self.keycode["'"]="'"
		self.keycode[":"]=":"
		self.keycode[";"]=";"
		self.keycode["/"]="/"
		self.keycode["\\"]="\\"
		self.keycode["("]="("
		self.keycode[")"]=")"
		self.keycode["["]="["
		self.keycode["]"]="]"
		self.keycode["{"]="{"
		self.keycode["}"]="}"
		self.keycode["<"]="<"
		self.keycode[">"]=">"
		self.keycode["+"]="+"
		self.keycode["-"]="-"
		self.keycode["!"]="!"
		self.keycode["?"]="?"
		self.keycode[","]=","
		self.keycode["0"]="0"
		self.keycode["1"]="1"
		self.keycode["2"]="2"
		self.keycode["3"]="3"
		self.keycode["4"]="4"
		self.keycode["5"]="5"
		self.keycode["6"]="6"
		self.keycode["7"]="7"
		self.keycode["8"]="8"
		self.keycode["9"]="9"
	
	def name(self):
		return "letter word code"