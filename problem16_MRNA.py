codon_table = {'UUU':'F',     'CUU':'L',      'AUU':'I',      'GUU':'V',
'UUC':'F',     'CUC':'L',      'AUC':'I',      'GUC':'V',
'UUA':'L',     'CUA':'L',      'AUA':'I',      'GUA':'V',
'UUG':'L',     'CUG':'L',      'AUG':'M',      'GUG':'V',
'UCU':'S',     'CCU':'P',      'ACU':'T',      'GCU':'A',
'UCC':'S',     'CCC':'P',      'ACC':'T',      'GCC':'A',
'UCA':'S',     'CCA':'P',      'ACA':'T',      'GCA':'A',
'UCG':'S',     'CCG':'P',      'ACG':'T',      'GCG':'A',
'UAU':'Y',     'CAU':'H',      'AAU':'N',      'GAU':'D',
'UAC':'Y',     'CAC':'H',      'AAC':'N',      'GAC':'D',
'UAA':'Stop',   'CAA':'Q',      'AAA':'K',      'GAA':'E',
'UAG':'Stop',   'CAG':'Q',      'AAG':'K',      'GAG':'E',
'UGU':'C',      'CGU':'R',      'AGU':'S',      'GGU':'G',
'UGC':'C',      'CGC':'R',      'AGC':'S',      'GGC':'G',
'UGA':'Stop',   'CGA':'R',      'AGA':'R',      'GGA':'G',
'UGG':'W',      'CGG':'R',      'AGG':'R',      'GGG':'G', }

amino_acid_counts = {}
for amino_acid in codon_table.values():
    if amino_acid in amino_acid_counts:
        amino_acid_counts[amino_acid] += 1
    else:
        amino_acid_counts[amino_acid] = 1
#print(amino_acid_counts)            
protein_string = input()
running_total = 1
for amino_acid in protein_string:
    running_total *= amino_acid_counts[amino_acid]
    total = (running_total * 3) % 1000000
print(total)
    
