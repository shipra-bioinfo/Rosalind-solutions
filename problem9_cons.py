import sys
data = sys.stdin.read().split('\n')
sequences = []
current_seq = ''
for line in data:
    if line.startswith('>'):
        if current_seq:
            sequences.append(current_seq)
            current_seq = ''
    else:
        current_seq += line
if current_seq:
    sequences.append(current_seq)
#print(sequences)  

length = len(sequences[0])
profile = {'A':[0]* length,
'C':[0]* length,
'G':[0]*length,
'T':[0]* length }
for seq in sequences:
    for i,base in enumerate(seq):
        profile[base][i] += 1
#print('Final profile:')

consensus = ''
for i in range(length):
    max_count = 0
    max_nuc = ''
    for nuc in 'ACGT':
        if profile[nuc][i] > max_count:
             max_count = profile[nuc][i]
             max_nuc = nuc
    consensus += max_nuc
print(consensus)
for nuc in 'ACGT':
    print(f"{nuc}: {' '.join(map(str,profile[nuc]))}")

