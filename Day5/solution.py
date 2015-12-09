import re
f = open("input.txt", "rt")

blacklist = re.compile('ab|cd|pq|xy')
vowels = "aeiou"

words = [word for word in f]
good_strings = 0

for word in words:
	if not blacklist.search(word):
		vow_num = 0
		for char in word:
			if char in vowels:
				vow_num+=1
		if vow_num >= 3:
			double_letter = False
			for i in range(len(word)-1):
				if word[i]==word[i+1]:
					double_letter = True
					break
			if double_letter:
				good_strings+=1

print good_strings	