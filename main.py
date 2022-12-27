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

if __name__=="__main__":
	text="1101 0010 0110000110 01 1 0011"
	
	text=text.upper()
	
	keycodes=[
		7,
		2,
		"SZYFR",
		"SZYFR",
		"SZYFR",
		("SZYFR", 3),
		("SZYFR", (2, 1)),
		("SZYFR", (1, 2)),
		"SZYFROWANIE",
		7,
		5,
		7,
		-7,
		7,
		5,
		35,
		("math", 1, 0),
		5,
		7,
		35,
		(1, 0),
		35,
		5,
		7,
		("math", 1, 0),
		5,
		35,
		7,
		(1, 0),
		7,
		35,
		5,
		35,
		5,
		7
	]
	
	keycode_to_keyboard_code={
		"(": "01",
		")": "10",
		"[": "101",
		"]": "010",
		"{": "001",
		"}": "100",
		"<": "1001",
		">": "0110",
		"\"": "110",
		"'": "011",
		" ": "0",
		"\n": "00",
		"\t": "000",
		".": "1",
		",": "11",
		"!": "111",
		"?": "1111",
		"/": "11111",
		"\\": "11111",
		":": "111111",
		";": "1111111",
		"+": "11111111",
		"-": "111111111",
		"A": "2",
		"Ą": "22",
		"B": "222",
		"C": "2222",
		"Ć": "22222",
		"D": "3",
		"E": "33",
		"Ę": "333",
		"F": "3333",
		"G": "4",
		"H": "44",
		"I": "444",
		"J": "5",
		"K": "55",
		"L": "555",
		"Ł": "5555",
		"M": "6",
		"N": "66",
		"Ń": "666",
		"O": "6666",
		"Ó": "66666",
		"P": "7",
		"Q": "77",
		"R": "777",
		"S": "7777",
		"Ś": "77777",
		"T": "8",
		"U": "88",
		"V": "888",
		"W": "9",
		"X": "99",
		"Y": "999",
		"Z": "9999",
		"Ź": "99999",
		"Ż": "999999"
	}
	
	keycode_to_letter_word_code={
		"A": "AGREGAT",
		"Ą": "ANTENA",
		"B": "BOMBA",
		"C": "CYLINDER",
		"Ć": "ĆWIEK",
		"D": "DOBROĆ",
		"E": "EKRAN",
		"Ę": "ENERGIA",
		"F": "FILTR",
		"G": "GRA",
		"H": "HENR",
		"I": "INDUKCJA",
		"J": "JĄDRO",
		"K": "KOMÓRKA",
		"L": "LAMPA",
		"Ł": "ŁOŻYSKO",
		"M": "MONITOR",
		"N": "NAPIĘCIE",
		"Ń": "NIEZMIENNOŚĆ",
		"O": "OMEGA",
		"Ó": "ÓSMY",
		"P": "PIORUN",
		"Q": "KUTER",
		"R": "ROTOR",
		"S": "SZKŁO",
		"Ś": "ŚRUT",
		"T": "TELEKOMUNIKACJA",
		"U": "URBANIZACJA",
		"V": "WIELOKROTNOŚĆ",
		"W": "WARIANCJA",
		"X": "KSERO",
		"Y": "YETI",
		"Z": "ZAŁĄCZNIK",
		"Ź": "ŹLEŹĆ",
		"Ż": "ŻADEN"
	}
	
	code_covers=[
		BasicInversionCode(),
		DoubleInversionCode(),
		GroupInversionCode(keycodes[0]),
		WordInversionCode(),
		SentenceInversionCode(),
		RandomFakeLetterCode(),
		AndFakeLetterCode(),
		OrFakeLetterCode(),
		XorFakeLetterCode(),
		ReversedFenceCode(keycodes[1]),
		BasicShuttleCode(),
		OutWordShuttleCode(),
		InWordShuttleWord(),
		TrailCode(keycodes[2]),
		AntiTrailCode(keycodes[3]),
		BasicSynchronousTrailCode(keycodes[4]),
		SynchronousTrailCode(keycodes[5][0], keycodes[5][1]),
		AsynchronousTrailCode(keycodes[6][0], keycodes[6][1]),
		AsynchronousTrailCode(keycodes[7][0], keycodes[7][1]),
		LetterWordCode(keycode_to_letter_word_code),
		AlphabetKeyCode(keycodes[8]),
		AlphabetVectorCode(keycodes[9]),
		AtBashCode(),
		AlphabetTableCode(keycodes[10]),
		AlphabetTableCode(keycodes[11]),
		AlphabetVectorCode(keycodes[12]),
		RaiseAlphabetCode(),
		RaisingGroupInversionCode(),
		NumberLetterConversion(),
		KeyboardCode(keycode_to_keyboard_code),
		GroupInversionCode(keycodes[13]),
		GroupInversionCode(keycodes[14]),
		FenceCode(keycodes[15]),
		ConversionCode(9),
		ConversionCode(8),
		ConversionCode(7),
		ConversionCode(6),
		ConversionCode(5),
		ConversionCode(4),
		ConversionCode(3),
		ConversionCode(2),
		ComplexCode(keycodes[16][0], keycodes[16][1], keycodes[16][2]),
		NumberLetterConversion(),
		KeyboardCode(keycode_to_keyboard_code),
		GroupInversionCode(keycodes[17]),
		GroupInversionCode(keycodes[18]),
		FenceCode(keycodes[19]),
		ConversionCode(9),
		ConversionCode(8),
		ConversionCode(7),
		ConversionCode(6),
		ConversionCode(5),
		ConversionCode(4),
		ConversionCode(3),
		ConversionCode(2),
		MixedComplexCode(keycodes[20][0], keycodes[20][1]),
		NumberLetterConversion(),
		KeyboardCode(keycode_to_keyboard_code),
		GroupInversionCode(keycodes[21]),
		GroupInversionCode(keycodes[22]),
		FenceCode(keycodes[23]),
		ConversionCode(9),
		ConversionCode(8),
		ConversionCode(7),
		ConversionCode(6),
		ConversionCode(5),
		ConversionCode(4),
		ConversionCode(3),
		ConversionCode(2),
		SumComplexCode(keycodes[24][0], keycodes[24][1], keycodes[24][2]),
		NumberLetterConversion(),
		KeyboardCode(keycode_to_keyboard_code),
		GroupInversionCode(keycodes[25]),
		GroupInversionCode(keycodes[26]),
		FenceCode(keycodes[27]),
		ConversionCode(9),
		ConversionCode(8),
		ConversionCode(7),
		ConversionCode(6),
		ConversionCode(5),
		ConversionCode(4),
		ConversionCode(3),
		ConversionCode(2),
		MixedSumComplexCode(keycodes[28][0], keycodes[28][1]),
		NumberLetterConversion(),
		KeyboardCode(keycode_to_keyboard_code),
		GroupInversionCode(keycodes[29]),
		GroupInversionCode(keycodes[30]),
		FenceCode(keycodes[31]),
		ConversionCode(9),
		ConversionCode(8),
		ConversionCode(7),
		ConversionCode(6),
		ConversionCode(5),
		ConversionCode(4),
		ConversionCode(3),
		ConversionCode(2),
		HuffmanCode(),
		NumberLetterConversion(),
		KeyboardCode(keycode_to_keyboard_code),
		GroupInversionCode(keycodes[32]),
		GroupInversionCode(keycodes[33]),
		FenceCode(keycodes[34]),
		ConversionCode(9),
		ConversionCode(8),
		ConversionCode(7),
		ConversionCode(6),
		ConversionCode(5),
		ConversionCode(4),
		ConversionCode(3),
		ConversionCode(2),
	]
	
	encode=QuadrupleCompressionCode().encode(text)
	decode=QuadrupleCompressionCode().decode(encode)
	
	exit