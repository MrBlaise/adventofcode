f = open("input.txt", "rt")
floor =0

for line in f:
    for char in line:
        if char == '(':
            floor += 1
        else:
            floor -= 1

print floor
