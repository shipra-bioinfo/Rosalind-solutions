from Bio import SeqIO

sequences = {}
for record in SeqIO.parse('rosalind_grph.fasta', 'fasta'):
    sequences[record.id] = str(record.seq)

for seq1_id, seq1 in sequences.items():
    for seq2_id, seq2 in sequences.items():
        if seq1_id != seq2_id:
            if seq1[-3:] == seq2[:3]:
                print(seq1_id, seq2_id)
