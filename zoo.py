numAni = int(input())
counter = 0
while numAni:
	counter += 1
	print("List {}:".format(counter))
	animals = {}
	for i in range(numAni):
		aniName = input().split()
		aniName = aniName[len(aniName)-1].lower()
		if aniName in animals.keys():
			animals[aniName] += 1
		else:
			animals[aniName] = 1
	for k, v in sorted(animals.items()):
		print("{} | {}".format(k, v))
	numAni = int(input())
