from Bio import SeqIO
sequences = [str(record.seq) for record in SeqIO.parse('rosalind_lcsm.fasta','fasta')]
shortest = min(sequences , key = len)
n = len(shortest)

for length in range(n, 0, -1):
    for start in range(n - length + 1):
        candidate = shortest[start:start+length]
        if all(candidate in seq for seq in sequences):
            print(candidate)
            break
    else:
        continue
    break 
