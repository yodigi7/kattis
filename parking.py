a, b, c = [int(x) for x in input().split()]

times = {"arrive":[], "leave":[]}
for i in range(3):
	time = [int(x) for x in input().split()]
	times["arrive"].append(time[0])
	times["leave"].append(time[1])

cars = 0
mostRecent = None
while times["arrive"] or times["leave"]:
	if not mostRecent:
		mostRecent = times["arrive"].pop(0)
	elif times["arrive"][0] == times["leave"][0]:
