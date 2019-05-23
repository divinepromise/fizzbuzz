def l33t(book_name):
	file = open(book_name)
	
	for line in file:
		word = line.strip()
		print(word)

		word = "aheiiager"

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

l33t("Book1.txt")
