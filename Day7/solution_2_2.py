# Source used: 
# https://www.reddit.com/r/adventofcode/comments/3vrsez/day_7_using_exec_in_python/

known = {}
f_in = open("input.txt", "rt")
for line in f_in:
    line = map(lambda s: s.strip(), line.split('->'))
    known[line[1].upper()] = line[0].replace('AND', '&').replace('OR', '|').replace('NOT ', '~').replace('RSHIFT', '>>').replace('LSHIFT', '<<').upper()

for i in range(200):
    B = 46065
    for val, expr in known.iteritems():
        try:
            exec(val + ' = (' + expr + ') & 65535')
        except Exception:
            pass

print "2. part A = ", A
