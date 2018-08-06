noteChanger = {'A#':'Bb', 'Bb':'A#', 'C#':'Db', 'Db':'C#', 'D#':'Eb', 'Eb':'D#', 'F#':'Gb', 'Gb':'F#', 'G#':'Ab', 'Ab':'G#'}
try:
    counter = 0
    while True:
        counter += 1
        info = input().split()
        answer = 'Case ' + str(counter) + ': '
        if info[0] in noteChanger:
            answer += noteChanger[info[0]] + ' ' + info[1]
        else:
            answer += 'UNIQUE'
        print(answer)
except:
    pass
