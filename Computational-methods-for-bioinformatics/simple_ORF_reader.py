from genbank import reverse_complement
from genbank import load_fasta
import re
    
    
def check_the_dna(load_fasta):
    
    start_codons_locations = []
    stop_codons_locations = []
    
    start_codons = re.compile('ATG')
    stop_codons = re.compile('TAG|TAA|TGA')
    
    p = start_codons.finditer(load_fasta)
    for i in p:
        start_codons_locations.append(i.start())
        
    o = stop_codons.finditer(load_fasta)
    for i in o:
        stop_codons_locations.append(i.end())
        
    cut = []

    cut2 = [load_fasta[x:y] for x in start_codons_locations for y in stop_codons_locations if len(load_fasta[x:y]) > 800]
   
    
    print(len(start_codons_locations))
    print(len(stop_codons_locations))
    print(len(cut2))
#    print(cut2)
    
    
'''
    
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

    
    

bounds_file = load_bounds('sequence.csv')
check_the_dna(fasta_file, bounds_file)
        
'''
    
fasta_file = load_fasta('gfap.fasta')
check_the_dna(fasta_file)
    
    
