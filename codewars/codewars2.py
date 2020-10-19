import re
p = re.compile('\d+') #cyfry [0-9]; procedura działania po użyciu re (tak działa re)
wynik = []

def order(sentence):
	slowo = sentence.split()	#podziel string na oddzielne słowa i utwórz listę, każde słowo jeden element
	
	cyfra = p.findall(sentence)	#znajdź w input wszystkie cyfry i stwórz z nich listę
			
	zipped = list(zip(cyfra, slowo)) #połącz listy z cyframi i oddzielonymi słowami (lista krotek)
	
	sort = sorted(zipped)	#ustaw w kolejności od najmn do najw wg pierwszego el. każdej krotki, czyli cyfry
		
	for k,v in sort:	#wybierz tylko druga wartosc z krotki (uszeregowanej), czyli słowo
		wynik.append(v)	#zapisz je do listy
	
	wynik2 = ' '.join(wynik)	#stwórz z listy string
		
	
	return wynik2	#zwróć wynik jako string (string input i string output)
		
	
order("Thi1s is2 3a T4est Fo1r the2 g3ood 4of th5e pe6ople")

