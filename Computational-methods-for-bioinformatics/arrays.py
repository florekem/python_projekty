import numpy

P = numpy.random.ranf([5,5])    #co za roznica czy () czy []?
print(P)
print()
print(P[1:3]) #wycinek z samych wierszy, od 2go do 3go
print()
print(P[:,1:3]) #wycinek z samych kolumn, od 2giej do 3ciej
print()
print(P[1:3, 2:4]) #wycinek kwadrata o krawędziach od wiersza 2go do 3go
                    #i jednoczesnie od kolumny 3ciej do 4tej
print()
v = [0,1,3]
h = [1,1,0]
print(P[v,h])   #printuje koordynaty na podstawie dwoch list: [0,1], [1,1], [3,0] 
                #robi iteracje najwyrazniej...
             
print()             

print(numpy.zeros((4,5)))   #tworzy pusta maciez, ktora mozna wykorzystac jako punkt wyjsciowy

print()
vector = [2,3,4]
o = numpy.ones(5)

print(o.sum())      #vektory to nie listy, mozna wywolywac na nich funkcje w ten sposob
print()

#example: extract values > 0.5 from P matrix

n,m = (P > 0.5).nonzero()   #ekstrahuje koordynaty i zapisuje w n,m (jak to dziala omgg??) 
                    #to wszystko zasluga numpy?
print(P[n,m])   #printuje wartosci pod tymi koordynatami
print()


#calculating distance from some point in the matrix (indices)

M = numpy.random.ranf((100,100))

x,y = numpy.indices(M.shape)
z = numpy.indices(M.shape)


x = x - 50      #japierd jakie to jest dziwne, on te wartosci wszystkie przechowuje w pamieci 
y = y - 40      # i wykonuje na nich dzialania i dalej jest macierza juz zmieniona.

dist = numpy.sqrt(x**2 + y**2)

#d = dist < 10  #tak samo tu, wynik to macierz True/False spelniajaca lub nie warunek

v,h = (dist < 10).nonzero() #zamiast powyrzej ^^ od razu koordynaty spelniajace warunek jako True 
print(dist[v,h])
print()
print(dist[v,h].mean())     #the average of the values that are within a distance of 10 from a point
                            # (averange of an area)
