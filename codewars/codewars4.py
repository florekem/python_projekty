def make_negative(number):
	if number > 0:
		wynik = '-' + str(number) 
		number2 = int(wynik)
		print(number2)
		return number2
	elif number == 0:
		return 0
	elif number < 0:
		print(number)
		return number	
	
		
make_negative(-6)
		
	
