import pickle
import urllib.request

what = pickle.load(urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p'))

#	[(' ', 14), ('#', 5), (' ', 70), ('#', 5), (' ', 1)]
#	mamy tutaj kilka tuple w liscie [(tuple), (tuple)]
#	kazdy tuple zawiera dwie wartosci (znak, liczba)
#	dwie wartośći w tuplach trzeba pomnożyć ze sobą
#	i połączyć w liście


for i in what: #gdzie i to kazda linia. kazda linia = jedna lista zawierajaca tuple[(), ()]
	mnozenie = ''.join([k * v for (k, v) in i]) # petla w petli, czyli w kazdej liscie 'i' dla tupla z wartosciami k,v pomnoz k *v
	print(mnozenie)
	
	
	
	#output z listy powyzej bez join():
	#	['              ', '#####', '                                                                      ', '#####', ' ']
	

