from Bio.Seq import Seq
with open("input.txt") as f:
    lines = f.read().split('\n')
sequences = {}
current_key = None
for line in lines:
    if line.startswith('>'):
        current_key = line[1:]
        sequences[current_key] = ""
    else:
        sequences[current_key] += line

keys = list(sequences.keys())
main_key = keys[0]
dna = sequences[main_key]
substrings = [sequences[k] for k in keys[1:]] 
for intron in substrings:
    dna = dna.replace(intron, "")

protein = Seq(dna).translate(to_stop  = True)
print(protein)     
