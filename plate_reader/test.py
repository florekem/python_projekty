import csv, re, os
from collections import defaultdict

sample_name	= 	[]

Ct 			= 	[]
detector	=	[]
zipped		= 	[]

filename = 'mimik.csv'

res = defaultdict(list)

def open_file():
	with open(filename, newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			global data = [str(row['Sample Name']), str(row['Detector']), row['Ct']]
	

def create_detector_list():
	open_file()

		if data[1] not in detector:
			detector.append(data[1])
			print(detector)
	return detector
	

create_detector_list()
		

"""

def create_detector_list(): 
	with open(plikcsv, newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			data = [str(row['Sample Name']), str(row['Detector']), row['Ct']]
			
			if data[1] not in detector:	 #zbiera info o detectorach
				detector.append(data[1])	
					
def create_data_list():
	with open(plikcsv, newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			data = [str(row['Sample Name']), str(row['Detector']), row['Ct']]

			for i in range(len(detector)):
				if detector[i] == data[1]: #zbiera info o nazwach probek i ct
					sample_name.append(detector[i] + "__" + data[0])
					Ct.append(data[2])
"""
