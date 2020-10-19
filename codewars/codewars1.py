def is_isogram(string):
	wyraz = []
	string = string.lower()
	for i in string:
		if i not in wyraz:
			wyraz.append(i)
		else:
			print('false')
			return False			
			break
	print(wyraz)
	return True

is_isogram('moOse')
