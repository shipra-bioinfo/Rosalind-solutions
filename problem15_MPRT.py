import requests
raw_ids = """P10153_RNKD_HUMAN
P01045_KNH2_BOVIN
P12923
Q05865
A4TI59
P01215_GLHA_HUMAN
O74366
P24000
A0QQ98
Q3BRP8
Q8ER84
P07725_CD8A_RAT"""
uniprot_ids = raw_ids.splitlines()

protein_sequences = {}
for uid in uniprot_ids:
    accession = uid.split("_")[0]
    url = f"https://rest.uniprot.org/uniprotkb/{accession}.fasta"
    response = requests.get(url)
    fasta_text = response.text
    lines = fasta_text.splitlines()
    sequence = "".join(lines[1:])
    protein_sequences[uid] = sequence
    #print(uid, len(sequence))

for uid, sequence in protein_sequences.items():
    positions = []
    for i in range(len(sequence) - 4 + 1):
        window = sequence[i:i+4]
        if window[0] == "N" and window[1] != "P" and (window[2] == "S" or window[2] == "T") and window[3] != "P":
            positions.append(i+1)
    if positions:
        print(uid)
        print(" ".join(str(p) for p in positions))
    