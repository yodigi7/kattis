cases = int(input())
for i in range(cases):
	line = input()
	if line == "P=NP":
		print("skipped")
	else:
		hold = line.split("+")
		print(int(hold[0])+int(hold[1]))
