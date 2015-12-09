from collections import defaultdict

f = open("input.txt", "rt")

moves = [move.strip() for line in f for move in line]
houses = defaultdict(int)
real_santa = [moves[i] for i in range(0, len(moves), 2)]
robo_santa = [moves[i] for i in range(1, len(moves), 2)]

houses[0, 0]+=1
def drop_gifts(commands):
	akt_x = 0
	akt_y = 0
	for move in commands:
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

drop_gifts(real_santa)
drop_gifts(robo_santa)
print len(houses.keys())