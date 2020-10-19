def minimum_number(numbers):
    
	
	iledodac = 0
	
	suma = sum(numbers)
	
	lista = []
	
	pierwsza = False
	
	while pierwsza == False:
	
		for liczba in range (2,suma):
			
			
			if suma % liczba == 0:
				lista.append(suma % liczba) #do listy reszte z dzielenia, czyli zawsze 0 dla nie pierwszej
		
		if len(lista) >= 1:
			suma += 1
			iledodac += 1
			lista = []
										
		else:
			pierwsza = True

	
	return(iledodac)
		
	
minimum_number([2,12,8,4,6])

"""
32 / 2 = 16
33 / 3 = 11
34 / 2 = 17
35 / 5 = 7


"""
    
    
    
    
    
    
