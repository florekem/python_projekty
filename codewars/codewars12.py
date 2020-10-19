import string

def is_pangram(s):
	
	s = s.lower()
	
	alphabet_str = 'abcdefghijklmnopqrstuvwxyz'
	lista = []
	
	for i in alphabet_str:
		for x in s:
			if i == x and x not in lista:
				lista.append(x)
				
	print(lista)
	
	if len(lista) == 26:
		return True
		
	else:
		return False
    




is_pangram("Pack my box with five dozen liquor jugs.")


"""
A pangram is a sentence that contains every single letter of the alphabet 
at least once. For example, the sentence "The quick brown fox jumps over 
the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. 
Ignore numbers and punctuation.


import string -> daje dostep do takich smaczkow jak caly alfabet, albo wszystkie cyfry:
string.ascii_lowercase -> alfabet malymi literami

print(string.ascii_lowercase)


https://docs.python.org/3.4/library/string.html?highlight=string%20module#string-constants



"""
