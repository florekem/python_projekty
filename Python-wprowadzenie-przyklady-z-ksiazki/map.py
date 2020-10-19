counters = [1, 2, 3, 4]

def inc(x):
	return x + 10
	
przyklad = map(inc, counters) # map(jaka funkcja, na czym funkcja ma byc wykonana)

print(list(przyklad))


#lambda w map (podmieniamy def przez lambde):

zamiast_def = map(lambda x: x + 10, counters) # w lambda masz polecenie

print(list(zamiast_def))

#filter i reduce - narzedzia programowania funkcyjnego
#podobnie jak map sa funkcjami wbudowanymi

odfiltruj = filter(lambda x: x > -4, range(-5, 3)) #tu w lambda masz warunek

print(list(odfiltruj))



#zamiast map mozna sie bawic w cos takiego:

def mymap(func, seq):
	res = []
	for x in seq:
		res.append(func(x))
	print(res)
		

mymap(inc, counters)


