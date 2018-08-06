class Person():
    def __init__(self):
        self.songs = []
        
    def addSong(self, song):
        self.songs.append(song)
        
    def getSongs(self):
        return self.songs

    def addSongList(self, songList):
        self.songs = songList

#Init variables
numVillagers = int(input())
numMeetings = int(input())
villagers = []
numSongs = 0

#Create villagers
for i in range(0, numVillagers):
    holder = Person()
    villagers.append(holder)

for i in range(0, numMeetings):
    newSong = False
    info = input().split()
    numPeople = int(info[0])
    totalSongs = []
    for j in range(1, numPeople+1):
        knownSongs = villagers[int(info[j])].getSongs()
        for k in range(0, len(knownSongs)):
            doKnow = False
            for l in range(0, len(totalSongs)):
                if knownSongs[k] == totalSongs[l]:
                    doKnow = True
            if not doKnow:
                totalSongs.append(knownSongs[k])
        if int(info[j]) == 1:
            newSong = True
    for j in range(1, numPeople+1):
        if newSong:
            villagers[int(info[j])].addSong(numSongs)
            numSongs += 1
        else:
            villagers[int(info[j])].addSongList(totalSongs)

for i in range(0, numVillagers):
    print("Villager " + str(i+1) + " knows:")
    print(villagers[i].getSongs())
                
