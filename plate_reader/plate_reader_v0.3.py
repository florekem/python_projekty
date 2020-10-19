import csv
from collections import defaultdict

sample_name	= 	[]

Ct 			= 	[]
detector	=	[]
zipped		= 	[]

plikcsv = input('podaj nazwe pliku: ')

res = defaultdict(list)



with open(plikcsv, newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		data = [str(row['Sample Name']), str(row['Detector']), row['Ct']]
		
		if data[1] not in detector:	 #zbiera info o detectorach
			detector.append(data[1])	
			
		for i in range(len(detector)):
			if detector[i] == data[1]: #zbiera info o nazwach probek i ct
				sample_name.append(detector[i] + "__" + data[0])
				Ct.append(data[2])
					
	
zipped = sorted(list(zip(sample_name, Ct))) #łączy dwie listy w jedną, sorted sortuje alfabetycznie;


for k,v in zipped:		
	if v != 'Undetermined':
		res[k].append(float(v))	#przyporządkowuje wartosc pierwszą z listy połączonej (k) jako klucz słownika
								# natomiast wartosc drugą (v) jako wartość klucza
								# wartości (tutaj 2 duplikaty ct) tworzą listę przyporządkowaną kluczowi
								# float zmienia str na liczbę przecinkową
								


f = open("output.csv", "w")


for k in res:						#dla każdego klucza w słowniku:
	wynik = sum(res[k]) / len(res[k])
	output = f.write(k + "," + str(wynik) + "\n")
	
print("\n" + 'Done')
	
										#oblicz średnią, czyli: jako że każdy klucz zawiera 
										#w sobie listę dwuelementową to: suma klucza (czyli listy)
										#podzielona na ilość ilementów klucza (listy) da średnią










