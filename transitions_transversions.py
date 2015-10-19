import sys
lines = sys.stdin.read().splitlines()

mappings = {"A": "G", "G": "A", "C": "T", "T": "C"}

strings = []
dna_string = ""
flag = False
for i in range(len(lines)):
    if ">" in lines[i]:
        if i > 0:
            strings.append(dna_string)
            dna_string = ""
    else:
        dna_string += lines[i]

strings.append(dna_string)

transitions = 0
transversions = 0

for i in range(len(strings[0])):
    if strings[0][i] == strings[1][i]:
        continue
    elif strings[0][i] == mappings[strings[1][i]]:
        transitions += 1
    else:
        transversions += 1

print(float(transitions)/transversions)
