cases = int(input())
for a in range(cases):
    dataset = input().split()
    dataset = [int(x) for x in dataset]
    sum2 = dataset[1]*dataset[1]
    sum3 = sum2 + dataset[1]
    sum1 = (dataset[1]*(dataset[1]+1))//2
    print(str(dataset[0]) + " " + str(sum1) + " " +  str(sum2) + " " +  str(sum3))