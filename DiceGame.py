def avg(x = []):
    average = 0
    for i in x:
        average += int(i)
    average /= len(x)
    return average

Gunnar = input().split()
Emma = input().split()

if avg(Emma) > avg(Gunnar):
    print("Emma")
elif avg(Emma) < avg(Gunnar):
    print("Gunnar")
else:
    print("Tie")
