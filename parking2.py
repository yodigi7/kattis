numCases = int(input())
for _ in range(numCases):
	numStores = int(input())
	stores = input().split()
	stores = [int(x) for x in stores]
	print((max(stores) - min(stores))*2)
