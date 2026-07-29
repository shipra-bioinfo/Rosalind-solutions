from Bio.Seq import Seq
seq = Seq(input())
rev_comp = seq.reverse_complement()
sequences = [seq, rev_comp]
orfs = set()
for s in sequences:
    for i in range(3):
        frame = s[i:].translate()
        for j, char in enumerate(frame):
            if char == 'M':
                k = j
                while frame[k] != '*' and k < len(frame) - 1:
                    k += 1
                    if frame[k] == '*':
                        orfs.add(frame[j:k])
                        
for orf in orfs:
    print(orf)                      
              