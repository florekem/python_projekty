def load_fasta(fasta_file):
    fasta_sequence = (''.join(open(fasta_file).readlines()[1:]).replace('\n', ''))
    return fasta_sequence

def load_bounds(bounds_file):
    file_open = open(bounds_file)
    file_read = file_open.read() #load file as string
    file_open.close()
    
    bounds = []
    bdata = file_read.split('\n')  #creates a list of strings in which each row is one entry
       
    for i in range(len(bdata) - 1):  # zamiast ponizszego if... 
        # if len(bdata[i]) > 1:   #pomija pierwsza liczbe [0] zmniejszajac ilosc krokow (i) i dlatego nie wywala bledu...
        cds_check, start, stop, cflag = bdata[i].split(',')
        if cds_check == 'CDS':
            bounds.append((int(start), int(stop), cflag)) #append tuple ( ) inside ( )
            
    return bounds

def reverse_complement(sequence):
    table = sequence.maketrans('ACGT', 'TGCA')
    
    st1 = sequence.translate(table)  #complement
    
    st1 = st1[::-1]  #reverse complement
    
    return st1

def gc_content(sequence, window = 128, step = 32):
    answ = []
    
    for i in range(0, len(sequence), step):
        cut = sequence[i:i+window].lower()
        a = cut.count('a')
        g = cut.count('g')
        c = cut.count('c')
        t = cut.count('t')
        ratio = float(c+g) / (a+c+g+t)
        answ.append(ratio)    
    
    return answ




