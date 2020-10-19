import genbank as gb
import numpy as np


def noncoding(fasta, bounds):
    answ = []
    for k in range(len(bounds) - 1):
        stop = bounds[k][1]
        start = bounds[k+1][0]
        if start-stop > 178:
            cut = fasta[stop:start-50]
            answ.extend(gb.gc_content(cut)) # append adds an element to a list, and extend concatenates the first list with another list
    return answ
        
    
def stats_of(inlist):   # uses numpy!
    vector = np.array(inlist)  # creates vector from a list
    return vector.mean(), vector.std()

    
    
    
    
    
    
fasta_file = gb.load_fasta('DNA.fasta')  
bounds_file = gb.load_bounds('sequence.csv')

noncoding(fasta_file, bounds_file)
print(stats_of(noncoding(fasta_file, bounds_file)))


