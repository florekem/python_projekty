import re
import zipfile


plik_zip_otworz = zipfile.ZipFile('channel.zip')

comments = []
number = '90052'

while True:	
	przeczytaj_w_txt = plik_zip_otworz.read(number + '.txt').decode('utf-8')
	comments.append(plik_zip_otworz.getinfo(number + '.txt').comment.decode('utf-8'))
			
	number_extract = re.search("\d+", przeczytaj_w_txt)
			
	if number_extract == None:
		break
	
	number = number_extract.group()
	
	print(number)
	
print(''.join(comments))
	
	

	
	



