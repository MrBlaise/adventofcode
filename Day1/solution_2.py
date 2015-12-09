f = open("input_2.txt", "rt")

def getPosBasement():
    floor =0
    pos = 0

    for line in f:
        for char in line:
            pos += 1
            if char == '(':
                floor += 1
            else:
                floor -= 1
            if floor == -1:
                return pos

print getPosBasement()
