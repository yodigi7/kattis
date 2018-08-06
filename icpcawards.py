numInp = int(input())
schools = []
schTeams = []
for i in range(numInp):
    line = input().split()
    if not line[0] in schools:
        schools.append(line[0])
        schTeams.append(" ".join(line))
counter = 0
for i in schTeams:
    counter += 1
    if counter > 12:
        break
    print(i)
