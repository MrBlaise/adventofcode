

f = open("input.txt", "rt")
lights = [[False for j in range(1000)] for i in range(1000)]

def toogleLights(instruction):
    start_x = int(instruction[0][0])
    start_y = int(instruction[0][1])
    dest_x = int(instruction[1][0])
    dest_y = int(instruction[1][1])

    y = start_y
    x = start_x
    while y < dest_y+1:
        x = start_x
        while x < dest_x+1:
            if lights[y][x]:
                lights[y][x] = False
            else:
                lights[y][x] = True
            x += 1
        y += 1

def turnLights(instruction, on_or_off):
    start_x = int(instruction[0][0])
    start_y = int(instruction[0][1])
    dest_x = int(instruction[1][0])
    dest_y = int(instruction[1][1])
    
    y = start_y
    x = start_x
    while y < dest_y+1:
        x = start_x
        while x < dest_x+1:
            lights[y][x] = on_or_off
            x += 1
        y += 1

instructions = [line.strip().split() for line in f]

for instruction in instructions:
    if instruction[0] == "toggle":
        from_to = []
        from_to.append(instruction[1].split(","))
        from_to.append(instruction[3].split(","))
        toogleLights(from_to)
    else:
        from_to = []
        from_to.append(instruction[2].split(","))
        from_to.append(instruction[4].split(","))
        on_or_off = instruction[1]
        if on_or_off == "off":
            on_or_off = False
        else:
            on_or_off = True
        turnLights(from_to, on_or_off)

def searchLights(lights):
    turned_on = 0
    for line in lights:
        for light in line:
            if (light):
                turned_on += 1
    return turned_on

print searchLights(lights)
"""
toggle 461,550 through 564,900
turn off 370,39 through 425,839
"""
