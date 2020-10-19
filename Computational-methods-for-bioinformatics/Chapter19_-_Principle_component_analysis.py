import numpy as np

array = np.array([[3,4,5,6,7],
                  [2,4,5,6,5],
                  [2,3,4,5,1],
                  [3,3,3,3,3]])



def pca(mat, D=2):  # D is a number of dimensions user want to keep
    a = mat - mat.mean(0)  # forcing matrix to have zero sum, so it does not induce energy into the system
    cv = np.cov(a.transpose())  # calculate covariance
    ev1, evc = np.linalg.eig(cv)  # calculate eigenvectors and eigenvalues
#    print(evc)
    V,H = mat.shape  # pobranie ilosci kolumn (H) i wierszy (V) matrycy
    cffs = np.zeros((V,D)) # = coefficients, are the locations of the data points in a new space
   
   # wybranie największych eigenvalues:
    ag = abs(ev1).argsort()  # zwraca indeksy wartosci (eigenvalues) od najmniejszej do najwiekszej
    ag = ag[::-1] # odwraca; indeksy od wartosci (eigenvalues) najwiekszej go najmniejszej
    me = ag[:D] # wybiera dwie największe eigenvalues [zakres od początku do D]
    print(me)
    ''' Those eigenvalues that are small are related to eigenvectors that
        are less important and it is these eigenvectors that can be discarded.
        
        w <me> na podstawie wielkosci eigenvalues,
        zapisane sa indeksy kolumn eigenwektorow. '''
    
    for i in range(V):  # dla i w range ilosci wierszy = 4
        k = 0
        for j in me: # dla j w liście najwiekszych eigenvalues
            cffs[i,k] = (mat[i] * evc[:,j]).sum() # wypelnienie pustej macierzy
            k += 1
            
    ''' kazdy wiersz mat[0-4] w macierzy mat pomnoz razy kolumne
        eigenwektorów evc, ktorej indeksy zapisane sa w <me>. '''
                    
    vecs = evc[:,me].transpose()
    ''' vecs are eigenvectors that are associated with the D (2) largest eigenvalues
        they were used to calculate new locations in loop above '''
   
    print(vecs)
    
    return cffs, vecs  # new locations, eingenvectors

def project(vecs, datavecs)
    

    
    
    
    
pca(array)




 
'''

print(array)   # array
print()
print(array.T)   #array transposed
print()
print(np.cov(array.transpose())) # covariance of transposed array
print()
array2 = np.random.ranf((1000,5)) * 10

print(np.cov(array2.transpose()))

'''

'''
# generating eigenvectors and eigenvalues using np.linalg.eig()
np.set_printoptions(precision = 3)

d = np.random.ranf((3,3))
A = np.dot(d, d.transpose())  #matrix multiplication, but using matmul or a @ b is preferred.

ev1, evc = np.linalg.eig(A)
print(ev1, evc)

'''