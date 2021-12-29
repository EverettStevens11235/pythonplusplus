version_ = "0.0.1"
state = "a"

tokens = []

def lexer(text):
	tok = ""
	inString = False
	string = ""
	for char in text:
		str(char)
		#check char
		if char == " ":
			if inString:
				string += char
			else:
				tok = ""
		elif char == '"':
			if inString:
				tokens.append("STRING: '" + string + "'")
				inString = False
			else:
				inString = True
		#check tok
		elif tok == "print":
			print("append print")
			tokens.append("PRINT")
			tok = ""
		#handles other characters
		else:
			if inString:
				string += char
	if tokens == []:
		return "No tokens found in line."
	else:
		return tokens
		
			
