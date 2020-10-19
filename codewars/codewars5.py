def gimme(input_array):
	
	sorted_array = sorted(input_array)
	
	middle_number = sorted_array[1]
	
	for i in input_array:
		if i == middle_number:
			wynik = input_array.index(i)
		
			return input_array.index(i)


gimme([2, 3, 1])
#gimme([1, 2, 3])
# 
