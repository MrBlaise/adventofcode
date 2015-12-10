f = open("input.txt", "rt")
boxes = []
totalPaper = 0

for line in f:
    array = line.strip().split('x')
    array = [int(x) for x in array]
    boxes.append(array)

for box in boxes:
    totalPaper += 2*box[0]*box[1] + 2*box[1]*box[2] + 2*box[0]*box[2]
    box.remove(max(box))
    totalPaper += box[0]*box[1]

print totalPaper
