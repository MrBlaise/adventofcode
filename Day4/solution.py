import md5
base = "yzbqklnj"

number = 1
while(True):
	m = md5.new()
	new_base = base + str(number)
	m.update(new_base)
	if m.hexdigest()[:5] == "00000":
		print number
		break;
	else:
		number += 1