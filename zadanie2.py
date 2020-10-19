
zadanie = open('szyfr.txt', 'r').read()

literki = 'abcdefghijklmnopqrstuwvwxyz'

for i in zadanie:
	if i in literki:
		print(i)

