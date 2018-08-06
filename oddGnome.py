numCases = int(input())
for _ in range(numCases):
	inp = [int(x) for x in input().split()]
	numGnomes = inp[0]
	list_ = inp[1:]
	for i in range(len(list_)):
		if i+2 == len(list_):
			print(i+1)
			break
		if list_[i] > list_[i+1] and list_[i] > list_[i+2]:
			print(i+1)
			break
		elif list_[i] > list_[i+1] and list_[i] < list_[i+2]:
			print(i+2)
			break
