def FirstFactorial(num): 
    
	lista = []
	x = 1
    
	for i in range(1, num + 1):
		lista.append(i)
		
	print(lista)
		
	for i in lista:

		x = x * i
		
	print(x)
    
    
    
FirstFactorial(8)
