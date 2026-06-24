dna = input('dna sequence:')
#complement
complement = dna.replace('A','t').replace('T','a').replace('C','g').replace('G','c')
complement = complement.upper()
#reverse
reverse_dna = complement[::-1]
print(reverse_dna)
