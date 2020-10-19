# nie koniecznie z tej ksiazki, tylko z tutoriala na yt.
# https://www.youtube.com/watch?v=xm25LaJANXc&t=0s&list=PLQVvvaa0QuDcJe7DPD0I5J-EDKomQDKsz&index=4


halite_dict = {(0,3): 100, (0,1): 200}  #kluczami moga byc krotki ;o

print(max(halite_dict, key=halite_dict.get))  # klucz, ktorego wartosc jest najwieksza
print(max(halite_dict))  # najwiekszy klucz

print('============')

direction_order = [(0,1), (1,1), (2,1), (2,2)]
position_options = [(10,20), (20,30), (30,40), (40,50)]

position_dict = {}

# tworzenie slownikow z dwoch np. list, ktore maja jednakowa ilosc elementow
for n, direction in enumerate(direction_order):  # enumerate pozwala loopowac position_options po indeksie
    position_dict[direction] = position_options[n]

print(position_dict)
print()    
print(dict(zip(direction_order, position_options)))  # robi to samo^^, chyba duzo latwiej? :)
print('============')

halite_dict = {}
halite_amount = [100, 200, 300, 400]

for direction in position_dict:
#    position = position_dict[direction]
    halite_dict[direction] = halite_amount
    
print(halite_dict)
    


