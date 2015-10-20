import sys
lines = sys.stdin.read().splitlines()

integer = int(lines[0])
initial = []
for i in range(1, integer+1):
    initial.append(i)

enumerations_list = []

def enumerations(string, numbers):
    if numbers:
        for j in numbers:
            if not str(j) in string:
                new_list = list(numbers)
                new_list.remove(j)
                enumerations(string + " " + str(j), new_list)
    else:
        enumerations_list.append(string)


for i in initial:
    new_list = list(initial)
    new_list.remove(i)
    enumerations(str(i), new_list)

print(len(enumerations_list))
for enum in enumerations_list:
    print(enum)
