def find_missing_letter(chars):
	#alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	alphabet_str = 'abcdefghijklmnopqrstuvwxyz'
	
	first_letter = []
	
	for i in alphabet_str:
		if i == chars[0].lower():
			first_letter.append(i)
	
	for x in alphabet_str:
		if x == first_letter:
		


find_missing_letter(['O','Q','R','S'])
