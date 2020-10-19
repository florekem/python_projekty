from genbank import reverse_complement
from genbank import load_fasta
from genbank import load_bounds
    
    
def check_the_dna(load_fasta, bounds):
    bad = []
    for i in range(len(bounds)):
        start, stop, cflag = bounds[i]  #rozpakowanie listy,
        cut = load_fasta[start-1:stop]
        
        if cflag == '-':
            cut = reverse_complement(cut)  #imported form genbank
        
        m3 = (stop - (start - 1)) % 3
        
        startcodon = cut[:3]
        stopcodon = cut[-3:]        

        if m3 == 0 and (startcodon == 'ATG' or startcodon == 'GTG' or startcodon == 'TTG') and (stopcodon == 'TAA' or stopcodon == 'TGA'):
            pass
        else:
            bad.append((start, stop, cflag))

    
    
fasta_file = load_fasta('DNA.fasta')  
bounds_file = load_bounds('sequence.csv')
check_the_dna(fasta_file, bounds_file)
        
