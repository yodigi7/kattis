inp = input().split()
fLimit = int(inp[0])
events = int(inp[1])
denied = 0
currIn = 0
for i in range(events):
	inp = input().split()
	num = int(inp[1])
	if inp[0] == "enter":
		if currIn + num > fLimit:
			denied += 1
		else:
			currIn += num
	else:
		currIn -= num
print(denied)
