def alphabet_position(text):
	alphabet_str = 'abcdefghijklmnopqrstuvwxyz'
	
	latwizna = list(enumerate(alphabet_str, 1))
		
	"""
	
	#ponizej dobry kod, ktory robi to samo, co enumerate()
	#powyzej mam stworzona liste od razu, ponizej krok po kroku
	
	
	
	text = text.lower()
	
	alph_list = []
	
	for i in alphabet_str:
		alph_list.append(i)
	
		
	whereisit = [pos + 1 for pos, char in enumerate(alphabet_str)]
		
	zipp = list(zip(alph_list,whereisit))
	print(zipp)
	
	"""
		
	output = []
	
	
	
	for i in text.lower():
		for number,letter in latwizna:
			if i == letter:
				output.append(str(number))
				
				
				
	print(" ".join(output))
	

	
	
alphabet_position("The sunset sets at twelve o' clock.")
