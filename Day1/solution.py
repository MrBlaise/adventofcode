with open("input.txt", "rt") as f:
    floor = sum([1 if char == "(" else -1 for line in f for char in line])
print floor

"""
for line in f:
    for char in line:
        if char == '(':
            floor += 1
        else:
            floor -= 1
"""
