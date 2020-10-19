import string

zadanie = "map"

trans = str.maketrans('abcdefghijklmnopqrstuwvwxyz', 'cdefghijklmnopqrstuwvwxyzab')

print(zadanie.translate(trans))

		

		
