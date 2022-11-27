from alphabet_code import *
from conversion_code import *
from fake_letter_code import *
from fence_code import *
from inversion_code import *
from keyboard_code import *
from shuttle_code import *
from trail_code import *

if __name__=="__main__":
	text="Nazywam się Ksawery Wawrzyniak."
	
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
		35
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
		ConversionCode(2)
	]
	
	encode=code_covers[31].encode(text)
	decode=code_covers[31].decode(encode)
	
	exit