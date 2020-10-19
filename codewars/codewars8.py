

"""
pytania:
1. Dlaczego po apostrofie (lub innym znaku z poza alfabetu .title() podnosi do uppercase?

c = "'"
	whereisit = [pos + 1 for pos, char in enumerate(words_upper) if char == c]
	
	to jakbym zapisal to tak:
		enum = enumerate(words_upper)
		[x for x, char in enum if char == c] -> iterator
		
		[x+1 for x,char in enum if char == c] 
		
		(x for x, char in enum if char == c) -> generator
	

rozpracowac to ^^

to co nizej w list comprehensions (rozwiazanie kogostam):

def toJadenCase(string):        
    return " ".join(w.capitalize() for w in string.split())


"""


def toJadenCase(string):
	words_upper = string.split()
	
	print(words_upper)

	lista = []
	
	for i in words_upper:
		lista.append(i.capitalize())
		
	out = " ".join(lista)
		
	return out
		

	




toJadenCase("chuj dupa kurwa jeban'amac")


