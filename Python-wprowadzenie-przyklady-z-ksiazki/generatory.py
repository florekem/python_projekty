def gensquares(N):
	for i in range(N):
		yield i ** 2
		
		
for i in gensquares(5):
	print(i, end = ' ')
	
	
# petla wywoluje funkcje, ktora zwraca pojedyncza wartosc do petli (ta printuje) 
# i loopuje dalej do funcji
# gdyby byl return funkcja zwrocilaby wartosc i przestala dzialac.
# tylko loop moze wywolac funkcje z yield.
# otrzymujemy funkcję, ktora ZWRACA WIELE wartosci, nie tylko jedna, zwrocona wartosc mozna
# wykorzystac do dalszych obliczen.

# jednorazowo mozna zwrocic wiele wartosci, gdy wynik loopa w funkcji umiescimy np. w liscie:

def buildsqueres(n):
	res = []
	for i in range(n):
		res.append(i**2)
	print(res)
	return res
	
	
buildsqueres(5)

# ale mamy liste i w liscie trzeba inaczej obrabiac wynik. w generatorze mamy pojedyncza wartosc.
