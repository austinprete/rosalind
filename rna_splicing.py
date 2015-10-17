import sys
lines = sys.stdin.read().splitlines()

dna_string = ""
introns = []

line_count = 0
for line in lines:
    if ">" in line:
        line_count += 1
        continue
    if line_count == 1:
        dna_string += line
    else:
        introns.append(line)

for i in introns:
    dna_string = "".join(dna_string.split(i))

rna_mappings = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V", "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V", "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V", "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V", "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A", "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A", "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A", "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A", "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D", "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D", "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E", "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E", "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G", "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G", "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G", "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}

dna_string = dna_string.replace("T", "U")

sequence_length = int(len(dna_string) / 3)

protein = ""
for i in range(sequence_length):
    sequence = dna_string[i*3:(i+1)*3]
    letter = rna_mappings[sequence]
    if letter == "Stop":
        break
    protein += letter

print(protein)
