import sys
# Read all lines from input
data = sys.stdin.read().split('\n')

sequences = {}
current_name = ''

for line in data:
    if line.startswith('>'):
        current_name = line[1:]
        sequences[current_name] = ''
    else:
        sequences[current_name] += line

# Calculate GC content for each sequence
best_name = ''
best_gc = 0

for name in sequences:
    dna =  sequences[name]
    if len(dna) == 0:
        continue
    gc = (dna.count('G') + dna.count('C')) / len(dna) * 100
    if gc > best_gc:
        best_gc = gc
        best_name = name

print(best_name)
print(best_gc)           
