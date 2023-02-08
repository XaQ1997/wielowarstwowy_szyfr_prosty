import csv
from datetime import *

from alphabet_code import *
from complex_code import *
from compression_code import *
from conversion_code import *
from fake_letter_code import *
from fence_code import *
from huffman_code import *
from inversion_code import *
from keyboard_code import *
from letter_word_code import *
from shuttle_code import *
from trail_code import *

class Coder:
	def __init__(self, code_covers, depth):
		try:
			self.code_covers=code_covers
			self.depth=depth
		except depth>len(code_covers):
			raise "ERROR!"
	
	def run(self, src_path, dst_path):
		with open(src_path) as src:
			text=src.read()
		
		with open(f"{dst_path}/layer_0.txt", "w") as layer0:
			layer0.write(text)
		
		with open(f"{dst_path}/coder_length.csv", "w", newline="") as length:
			filewriter=csv.writer(length, delimiter=";")
			filewriter.writerow(["layer", "length", "time"])
			filewriter.writerow(["0", f"{len(text)}", f"{datetime.now()}"])
		
		for i in range(self.depth):
			with open(f"{dst_path}/layer_{i+1}.txt", "w") as layer:
				if self.code_covers[i].name()=="compression code":
					text, lines=self.code_covers[i].encode(text)
					
					for i in range(len(lines)):
						with open(f"{dst_path}/compressing_results/{i}.txt", "x") as result:
							result.write(lines[i])
				else:
					text=self.code_covers[i].encode(text)
				layer.write(text)
			
			with open(f"{dst_path}/coder_length.csv", "a+", newline="") as length:
				filewriter=csv.writer(length, delimiter=";")
				filewriter.writerow([f"{i+1}", f"{len(text)}", f"{datetime.now()}"])
		
		return text

class Decoder:
	def __init__(self, code_covers, depth):
		try:
			self.code_covers=code_covers
			self.depth=depth
		except depth>len(code_covers):
			raise "ERROR!"
	
	def run(self, path):
		with open(f"{path}/layer_{self.depth}.txt") as src:
			text=src.read()
		
		with open(f"{path}/decoder_length.csv", "w", newline="") as length:
			filewriter=csv.writer(length, delimiter=";")
			filewriter.writerow(["layer", "time"])
			filewriter.writerow([f"{self.depth}", f"{datetime.now()}"])
		
		for i in range(self.depth):
			text = self.code_covers[i].decode(text)
			
			with open(f"{path}/decoder_length.csv", "a+", newline="") as length:
				filewriter = csv.writer(length, delimiter=";")
				filewriter.writerow([f"{self.depth-i-1}", f"{datetime.now()}"])
		
		return text