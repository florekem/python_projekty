import urllib.request
import re


number = '8022'

while True:
	
	page="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + number
	content = urllib.request.urlopen(page)
	
	przeczytaj = content.read().decode('utf-8')

	number_extract = re.search('\d+', przeczytaj)
	
	number = number_extract.group()
	
	
	print(number)
	
	
	

	
	


