import re
import itertools
from string import ascii_lowercase

f = open("input.txt", "rt")
product_generator = itertools.product(ascii_lowercase, repeat=2)
product = [p for p in product_generator]
words = [word.strip() for word in f]
good_strings = 0

for word in words:
	repeat_two = False
	for i in product:
		if word.count(''.join(i)) >= 2:
			repeat_two = True
			break

	double_letter = False
	for i in range(len(word)-2):
		if word[i]==word[i+2]:
			double_letter = True
			break

	if double_letter and repeat_two:
		good_strings+=1

print good_strings	