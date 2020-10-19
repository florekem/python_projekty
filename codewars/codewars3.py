def sort_array(source_array):
	
	odd_list = []
	
	even_list = [] #even list powinna zawierac koordynat, czyli lista krotek
	even_position = []
	even_number = []
	
#	mixed_list = []
	
	
	for i in source_array: #jesli przyste zostaja na miejscu
		if i % 2 == 0:
			#check at what position even numbers are
			position_check = source_array.index(i)
			even_position.append(position_check)
			even_number.append(i)
		else:
			odd_list.append(i)
	
	even_list = list(zip(even_number, even_position))
	print(even_list)
	sorted_odd_list = sorted(odd_list)	
	print(sorted_odd_list)	
	
	#do listy posortowanych nieparzystych dodaj zapamietane pozycje parzystych liczb
	
	
	for cyfra, pozycja in even_list:
		sorted_odd_list.insert(pozycja, cyfra)
	
	
	print(sorted_odd_list)	
	
	
	return sorted_odd_list	
	
			
			
			
sort_array([5, 3, 2, 8, 1, 4])
		
		
		
