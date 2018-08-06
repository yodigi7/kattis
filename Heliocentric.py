class Planet():
    def __init__(self, fullCycle, today):
        self.fullCycle = fullCycle
        self.today = today

    def oneDay(self):
        self.today += 1
        if self.today == self.fullCycle:
            self.today = 0
            return True
        return False

done = False
case = 0

while not done:
    try:
        case += 1
        info = input().split()
        earthIsZ = earthStart = int(info[0])
        marsIsZ = marsStart = int(info[1])
        earth = Planet(365, earthStart)
        mars = Planet(687, marsStart)
        earthIsZ = not earthIsZ
        marsIsZ = not marsIsZ
        days = 0
        while not earthIsZ or not marsIsZ:
            earthIsZ = earth.oneDay()
            marsIsZ = mars.oneDay()
            days += 1
        print("Case " + str(case) + ": " + str(days))
        
    except:
        done = True
