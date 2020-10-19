def nb_year(p0, percent, aug, p):
	
	percent_dec = percent / 100
	
	years = 0
	
	while p0 < p:
		p0 = p0 + (p0 * percent_dec) + aug
		
		years += 1
	
	return years
	
	
	
	
	
	
	
nb_year(1500, 5, 100, 5000)
