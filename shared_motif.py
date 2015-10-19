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

shortest = strings[0]
for i in strings[1:]:
    if len(i) < len(shortest):
        shortest = i

def is_in_all(s):
    for string in strings:
        if not s in string:
            return False
    return True

substrings = []
should_continue = True
for i in reversed(range(len(shortest))):
    if not should_continue:
        break
    for j in reversed(range(len(shortest) - i)):
        string = (shortest[j:j+i+1])
        if is_in_all(string):
            print(string)
            should_continue = False
            break
