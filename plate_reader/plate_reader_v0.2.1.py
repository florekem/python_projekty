# wersja ze słownikami zamiast list
# każdy detector będzie miał własny słownik (zakładany automatycznie na podstawie pliku)
# jeśli klucz w słowniku może mieć kilka wartości
# 

# mir92 = {
#	'K1': [1, 2], 'K2': [1, 2], 'K3': [1, 2], 'MC1': [1, 2] (...)
#	}

#policz średnią dla każdego klucza, wyprintuj średnie




import csv, re, os


sample_name1 = 	[]
sample_name2 = 	[]
sample_name3 = 	[]
Ct1			= 	[]
Ct2			= 	[]
Ct3			= 	[]
detector	=	[]


def list_detectors(): #listuje detectory
	with open(plikcsv, newline='') as f:
		reader = csv.DictReader(f)
		for row in reader:
			data = [str(row['Detector'])]
			if data[0] not in detector:		# sprawdza czy dany detector jest już w liście detectorów
				detector.append(data[0])	# PLAN: powstanie słowników dla każdego detectora
		print(detector)

def create_data_list(): # tworzy 2 listy z danymi: sample name i Ct
	with open(plikcsv, newline='') as f:
		reader = csv.DictReader(f)
		for row in reader:
			data = [str(row['Sample Name']), str(row['Detector']), row['Ct']]
			if detector[0] == data[1]:
				sample_name1.append(data[0])
				Ct1.append(data[2])
			if detector[1] == data[1]:
				sample_name2.append(data[0])
				Ct2.append(data[2])
			if detector[2] == data[1]:
				sample_name3.append(data[0])
				Ct3.append(data[2])
'''				
def oblicz_srednia(sample_type):
	do_sredniej	= 	[]
	
	for i in range(minimum_sample_no, maximum_sample_no):
		sample_no = sample_type + str(i) + after_sample_name_and_number

		for k,v in zipped:
			if k == sample_no:
				do_sredniej.append(float(v))
			
		srednia = sum(do_sredniej) / len(do_sredniej)
		
		print(srednia)
		
	do_sredniej = []

#start programu:
#1) print wszystkich plików w katalogu --> jak zastosować do katalogu w którym jest plik?
#2) podanie nazwy pliku --> jak zrobić wybór typu 1)plik1 2)plik2
#3) wylistowanie detectorów w danym pliku
#4) wybranie detectora --> jak zrobic: 1) jak w przypadku wyboru pliku; 2) całkowita automatyzacja bez wyboru detectora i liczby n... ale to w chuj trudne ;)
#5) utworzenie dla danego detectora listy krotek z danymi 
print(os.listdir(path='/home/maciek/Seafile/Moja biblioteka/python_projekty/plate_reader'))
'''

plikcsv = input("nazwa pliku: ")	
list_detectors()
#podaj_detector = input("Podaj DETECTOR: ")
create_data_list()
		
zipped1 = sorted(list(zip(sample_name1, Ct1)))
zipped2 = sorted(list(zip(sample_name2, Ct2)))
zipped3 = sorted(list(zip(sample_name3, Ct3))) # sorted sortuje alfabetycznie; czy to jest potrzebne?
print(detector[0])
print(zipped1)
print(detector[1])
print(zipped2)
print(detector[2])
print(zipped3)								# po zip uzyskujemy krotke (tuple) dwuelementową

'''


while True:
	number_of_samples = input("max sample no: ")
	minimum_sample_no = int(input("minimum sample no: "))
	maximum_sample_no = int(number_of_samples)+1
	after_sample_name_and_number = input("After sample name and number: ")
	oblicz_srednia(input('before sample name and number' ))
		
		
# kolejnosc numerowania: co jesli nie bedzie jakiegos numeru?
# automatyczny wybor detectora (pod numerem)

'''
do_sredniej = []

while True:

	podaj_nazwe_probki = input("podaj nazwę próbki: ")



	print(detector[0])
	print(podaj_nazwe_probki)

	for k,v in zipped1:
		
		if k == podaj_nazwe_probki:
			do_sredniej.append(float(v))
			
			
	srednia = sum(do_sredniej) / len(do_sredniej)
			
	print(srednia)
	do_sredniej = []

	print(detector[1])
	print(podaj_nazwe_probki)

	for k,v in zipped2:
		
		if k == podaj_nazwe_probki:
			do_sredniej.append(float(v))
			
			
	srednia = sum(do_sredniej) / len(do_sredniej)
			
	print(srednia)
	do_sredniej = []

	print(detector[2])
	print(podaj_nazwe_probki)

	for k,v in zipped3:
		
		if k == podaj_nazwe_probki:
			do_sredniej.append(float(v))
			
			
	srednia = sum(do_sredniej) / len(do_sredniej)
			
	print(srednia)
	do_sredniej = []
