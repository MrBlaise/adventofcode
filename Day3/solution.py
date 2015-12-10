from collections import defaultdict

f = open("input.txt", "rt")

moves = [move.strip() for line in f for move in line]
houses = defaultdict(int)
akt_x = 0
akt_y = 0

houses[akt_x, akt_y]+=1
for move in moves:
	if move == '>':
		akt_y+=1
		houses[akt_x, akt_y]+=1
	elif move == '<':
		akt_y-=1
		houses[akt_x, akt_y]+=1
	elif move == '^':
		akt_x+=1
		houses[akt_x, akt_y]+=1
	elif move == 'v':
		akt_x-=1
		houses[akt_x, akt_y]+=1

print len(houses.keys())