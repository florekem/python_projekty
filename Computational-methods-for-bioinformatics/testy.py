def MA():
	intens = 3
	backg = 1
	vals = intens - backg
	print(vals)
	mask = vals > 0					#usuniecie wartosci mniejszych od zera
	vals = mask*vals + (1-mask)*1
	print(vals)

MA()
