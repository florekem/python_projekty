def getMoneySpent(keyboards, drives, b):
	lista = []
	for i in keyboards:
		for x in drives:
			if i + x < b:
				lista.append(x+i)
			elif i + x > b and len(lista) = 0:
				return -1
			
	 
	return max(lista)
    
    
getMoneySpent(keyboards = [3,1], drives = [5,2,8], b = 10)
