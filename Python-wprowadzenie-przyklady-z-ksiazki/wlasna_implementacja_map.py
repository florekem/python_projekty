counters = [1, 2, 3, 4]
counters2 = [5,6,7,8]




def inc(*x):
	print(list(zip(*x)))	#rozpakowuje dowolna liczbe argumentow, zip laczy w nowe sekwencje
	
inc(counters, counters2)

"""
def inc(*x):
	for args in zip(*x):	#wywolanie rozpakowuje dowolna liczbe argumentow, laczac je w nowe sekwencje
		print(args)			
	


"""

def mymap2(func, *seqs):
	res = []
	for swargs in zip(*seqs):
		res.append(func(*swargs))		#jesli jest samo args mowi ze pow potrzebuje wiecej niz 1 argument
		
	print(res)

		

		
mymap2(pow, counters, counters2)
		



