f = open("input.txt", "rt")
boxes = []
totalRibon = 0

for line in f:
    array = line.strip().split('x')
    array = [int(x) for x in array]
    boxes.append(array)

for box in boxes:
    totalRibon += box[0]*box[1]*box[2]
    box.remove(max(box))
    totalRibon += 2*box[0] + 2*box[1]

print totalRibon
