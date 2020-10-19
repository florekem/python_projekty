def find_even_index(arr):
	suma = sum(arr)
	
	
	dlugosc = len(arr)
	i = 0
	
	
	if sum(arr[1:dlugosc]) == 0: # jesli suma wszystkich po pierwszej liczbie == 0
		#print(0)				#zwroc 0 jako indeks (bo z lewej tez jest 0 i indeks 0 jest po srodku)
		return 0
		
	if sum(arr[0:len(arr)-1]) == 0:
		#print(len(arr) - 1)
		return len(arr) - 1
		
	
	while i < dlugosc:
		lewa = sum(arr[0:0+i+1])
		prawa = sum(arr[2+i:dlugosc]) 
		
		if  lewa == prawa:
			#print("lewa: " + str(lewa))
			#print("prawa: " + str(prawa))
			
			#print(i)
			indeks = i + 1
			#print(indeks)
			return indeks
						
		
		else:
			#print("lewa: " + str(lewa))
			#print("prawa: " + str(prawa))
			i += 1	
			
			
	if i == len(arr):
		#print("-1 dziwko")
		return -1
		

    
    
    
find_even_index([1,2,3,4,3,2,1])
#find_even_index([20,10,-80,10,10,15,35])

#find_even_index([10,-80,10,10,15,35,20])


"""

def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1




Input:
An integer array of length 0 < arr < 1000. The numbers in the array can be any 
integer positive or negative.

Output:
The lowest index N where the side to the left of N is equal to the side to the 
right of N. If you do not find an index that fits these rules, then you will return -1.

Note:
If you are given an array with multiple answers, return the lowest correct index.
An empty array should be treated like a 0 in this problem. 



Test.assert_equals(find_even_index([1,100,50,-51,1,1]),1,)
Test.assert_equals(find_even_index([1,2,3,4,5,6]),-1)
Test.assert_equals(find_even_index([20,10,30,10,10,15,35]),3)
Test.assert_equals(find_even_index([20,10,-80,10,10,15,35]),0)
Test.assert_equals(find_even_index([10,-80,10,10,15,35,20]),6)
Test.assert_equals(find_even_index(range(1,100)),-1)


"""
