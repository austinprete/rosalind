import sys
lines = sys.stdin.read().splitlines()



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
