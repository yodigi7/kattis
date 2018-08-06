info = input().split()
numAirports, numRoutes = [int(x) for x in info]

class Airport():
    def __init__(self, num):
        self.portNum = num
        self.shownTimes = 0
        self.hasLounge = None

    def addToRoute(self):
        self.shownTimes += 1

    def getShownTimes(self):
        if self.hasLounge == None:
            return self.shownTimes
        return 0

class Route():
    def __init__(self, airport1, airport2, lounges):
        self.port1 = airport1
        self.port2 = airport2
        self.lounges = lounges

numLounges = 0
ports = {}
routes = []
for i in range(numRoutes):
    delList = []
    info = input().split()
    port1, port2, lounges = [int(x) for x in info]
    if port1 in ports:
        ports[port1].addToRoute()
    else:
        ports[port1] = Airport(port1)
    if port2 in ports:
        ports[port2].addToRoute()
    else:
        ports[port2] = Airport(port2)
    currRoute = Route(ports[port1], ports[port2], lounges)
    routes.append(currRoute)
    
    #if needs lounge and must not have one
    if lounges == 2 and (ports[port2].hasLounge == False or ports[port1].hasLounge == False):
        print('impossible')
        break
    #if needs no lounges and must have one
    elif lounges == 0 and (ports[port2].hasLounge == True or ports[port1].hasLounge == True):
        print('impossible')
        for i in reversed(range(len(routes))):
            delList.append(i)
        for i in delList:
            del routes[i]
        break
    elif lounges == 2:
        if ports[port1].hasLounge == None:
            numLounges += 1
        if ports[port2].hasLounge == None:
            numLounges += 1
        ports[port1].hasLounge = True
        ports[port2].hasLounge = True
        routes.remove(currRoute)
    elif lounges == 0:
        ports[port1].hasLounge = False
        ports[port2].hasLounge = False
        routes.remove(currRoute)

while routes:
    maxPort = None
    maxShown = 0
    delList = []
    found = False
    for i in ports.values():
        print(i.getShownTimes())
        if i.getShownTimes() > maxShown:
            maxShown = i.getShownTimes()
            maxPort = i
            found = True
            print(maxPort)
    if found:
        maxPort.hasLounge = True
        numLounges += 1
    else:
        break
    for i, route in reversed(list(enumerate(routes))):
        if route.port1.hasLounge == True and route.port2.hasLounge == True and route.lounges == 1:
            print('impossible')            
        if route.port1.hasLounge == True or route.port2.hasLounge == True:
            delList.append(i)
    for i in delList:
        del routes[i]

#print answer
print(numLounges)
