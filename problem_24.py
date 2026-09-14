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

def find_overlap(a, b):
    n = min(len(a), len(b))

    for overlap_len in range(n, 0, -1):
        if a[-overlap_len:] == b[:overlap_len]:
            return overlap_len

    return 0

while len(sequences) > 1:
    best_overlap = 0
    best_i = -1
    best_j = -1
    best_order = None

    for i in range(len(sequences)):
        for j in range(i + 1, len(sequences)):
            overlap_ij = find_overlap(sequences[i], sequences[j])
            overlap_ji = find_overlap(sequences[j], sequences[i])

            if overlap_ij > best_overlap:
                best_overlap = overlap_ij
                best_i = i
                best_j = j
                best_order = "ij"

            if overlap_ji > best_overlap:
                best_overlap = overlap_ji
                best_i = i
                best_j = j
                best_order = "ji"

    if best_i == -1:
        merged = sequences[0] + sequences[1]
        best_i = 0
        best_j = 1
    elif best_order == "ij":
        merged = sequences[best_i] + sequences[best_j][best_overlap:]
    else:
        merged = sequences[best_j] + sequences[best_i][best_overlap:]

    new_sequences = []

    for idx, sequence in enumerate(sequences):
        if idx != best_i and idx != best_j:
            new_sequences.append(sequence)

    new_sequences.append(merged)
    sequences = new_sequences

if sequences:
    print(sequences[0])