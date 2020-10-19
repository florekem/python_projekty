lista = [1,2,5]
lista_dup = [1,2,5]


wynik = [abs(x - y) for x in lista for y in lista_dup]
    

print(wynik)
print(max(wynik))