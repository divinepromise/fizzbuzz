def l33t():

	try:
		userinput = input("enter the exact bookname with its extension\n")

		file = open(userinput)
	
		for line in file:
			word = line.strip()
			
			if word.endswith("er"):
				strip = word[:-2]
				new_word = strip + "xor"
	
			for char in new_word:
				if char == "o" or "O":
					char = 0
				elif char == "a" or "A":
					char = 4
				elif char == "e" or "E":
					char = 3
				elif char == "i" or "I":
					char = 1
			print(new_word)
	except:
		print("please enter a string value")



l33t("Book1.txt")
