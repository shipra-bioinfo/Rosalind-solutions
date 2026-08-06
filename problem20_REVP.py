from Bio.Seq import Seq
seq = Seq(input())
for length in range(4, 13):
    for start in range(len(seq) - length + 1):
        substring = seq[start : start + length]
        if substring == substring.reverse_complement():
            print(start + 1, length)   #Rosalind uses 1-indexed position but python indexing starts at 0 so add 1 when reporting the position. 
