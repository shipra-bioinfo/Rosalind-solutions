import sys
lines = sys.stdin.read().split('\n')
some_list = lines[1].split()
seq = [int(x) for x in some_list]
lengths = [1] * len(seq)
prev = [-1] * len(seq)
for i in range(1, len(seq)):
    for j in range(0, i):
        if seq[i] > seq[j]:
            if lengths[j] + 1 > lengths[i]:
                lengths[i] = lengths[j] + 1
                prev[i] = j
#print(lengths)
#print(prev)
best_index = lengths.index(max(lengths))
result = [seq[best_index]]
while prev[best_index] != -1:
    best_index = prev[best_index]
    result.append(seq[best_index])
result.reverse()
print(' '.join(str(numb) for numb in result))   

lengths2 = [1] * len(seq)
prev2 = [-1] * len(seq)
for i in range(1, len(seq)):
    for j in range(0, i):
        if seq[i] < seq[j]:
            if lengths2[j] + 1 > lengths2[i]:
                lengths2[i] = lengths2[j] + 1
                prev2[i] = j
best_index2 = lengths2.index(max(lengths2))
result2 = [seq[best_index2]]
while prev2[best_index2] != -1:
    best_index2 = prev2[best_index2]
    result2.append(seq[best_index2])
result2.reverse()
print(' '.join(str(numb) for numb in result2))       
