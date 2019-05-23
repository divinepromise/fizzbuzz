'''
1. Find words in Books that are non present in 20k.txt [Do it for each book]
2. Find words in the 20k.txt that are non present in any Books
3. Write the result of part (1) to bookXuniqu.list [X is the book number]
4. Write the result of part (2) to rarewords.list
'''

import string

def non_present(*args):
	lst = []
	for arg in args:
		lst.append(unfound_words(arg))
	i = 1
	while i < 4:
		new_file = open('book'+[i]+"uniqui.list", "w")
		newfile.write(lst)
		i +=1

def unfound_words(bookname):
	d1 = dict()
	l



non_present("Book1.txt","Book2.txt","Book3.txt")


