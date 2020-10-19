def intersect(*args): #krzyzowanie jednej krotki z druga -> jesli x z 1wszej jest w kolejnej krotce to dodaj do listy
	res = []
	for x in args[0]:
		for other in args[1:]:
			if x in other and x not in res: #dopiero teraz jest ZBIOR czesci wspolnej jaka s2 i s3 dziela z s1
				res.append(x)
			else:
				break
	print(res)
	
s1, s2, s3 = "Teodor", "Teofil", "Troll" 

intersect(s1, s2, s3) 	# wynik zalezny jest od tego, ktora wartosc jest pierwsza

def union(*args): # ZBIOR -> kazdy element ze zbioru wystepuje tylko raz, jesli nie ma jeszcze x to dodaj do listy
	res = []
	for seq in args:
		for x in seq:
			if x not in res:
				res.append(x)
	print(res)
	
	
union(s1, s2)


