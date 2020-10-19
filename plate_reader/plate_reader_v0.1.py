import csv, re, os


sample_name	= 	[]
Ct 			= 	[]



def openfile(plikcsv): #otwiera plik
	with open(plikcsv, newline='') as f:
		reader = csv.DictReader(f)
		for row in reader:
			data = [str(row['Sample Name']), str(row['Detector']), row['Ct']]
			if podaj_detector == data[1]:
				sample_name.append(data[0])
				Ct.append(data[2])
				
def oblicz_srednia(x):
	do_sredniej	= 	[]
	
	for i in range(1, maximum_sample_no):
			
		sample_type = x		
		sample_no = sample_type + str(i) + after_sample_name_and_number

		for k,v in zipped:
			if k == sample_no:
				do_sredniej.append(float(v))
			
		srednia = sum(do_sredniej) / len(do_sredniej)
		
		print(srednia)
		
	do_sredniej = []


print(os.listdir(path='/home/maciek/Seafile/Moja biblioteka/python_projekty/plate_reader'))
plikcsv = input("nazwa pliku: ")
podaj_detector = input("Podaj DETECTOR: ")
openfile(plikcsv)
		
zipped = sorted(list(zip(sample_name, Ct))) # sorted sortuje alfabetycznie;
print(zipped)								# po zip uzyskujemy krotke (tuple) dwuelementową

number_of_samples = input("Podaj n: ")
maximum_sample_no = int(number_of_samples)+1


while True:
	after_sample_name_and_number = input("After sample name and number: ")
	oblicz_srednia(input('K czy MC:' ))
		
		
# kolejnosc numerowania: co jesli nie bedzie jakiegos numeru?
# automatyczny wybor detectora (pod numerem)



	




