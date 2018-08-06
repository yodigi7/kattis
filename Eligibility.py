numCases = int(input())

for i in range(0, numCases):
    status = ''
    info = input().split()
    name = info[0]
    postSecond = info[1].split('/')
    bDate = info[2].split('/')
    numCourses = int(info[3])
    
    for j in range(0, len(postSecond)):
        postSecond[j] = int(postSecond[j])
        bDate[j] = int(bDate[j])

    if postSecond[0] >= 2010:
        status = "eligible"
    elif bDate[0] >= 1991:
        status = "eligible"
    elif numCourses >= 41:
        status = "ineligible"
    else:
        status = "coach petitions"

    answer = name + " " + status
    print(answer)
    
