answers = []
Adrian = []
Bruno = []
Goran = []
aScore = 0
bScore = 0
cScore = 0
leader = "Adrian"
maxScore = 0

questions = int(input())
answersStr = input()
answers = list(answersStr)

for i in range(0, ((questions-1)//3)+1):
    Adrian.append("A")
    Adrian.append("B")
    Adrian.append("C")
    Bruno.append("B")
    Bruno.append("A")
    Bruno.append("B")
    Bruno.append("C")
    Goran.append("C")
    Goran.append("C")
    Goran.append("A")
    Goran.append("A")
    Goran.append("B")
    Goran.append("B")

for i in range(0, questions):
    if answers[i] == Adrian[i]:
        aScore += 1
    if answers[i] == Bruno[i]:
        bScore += 1
    if answers[i] == Goran[i]:
        cScore += 1
    if aScore > bScore and aScore > cScore:
        leader = "Adrian"
        maxScore = aScore
    elif aScore < bScore and bScore > cScore:
        leader = "Bruno"
        maxScore = bScore
    elif cScore > aScore and cScore > bScore:
        leader = "Goran"
        maxScore = cScore

print(maxScore)

if aScore == maxScore:
    print("Adrian")
if bScore == maxScore:
    print("Bruno")
if cScore == maxScore:
    print("Goran")
