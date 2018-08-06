class MosquitoGroup:
    def __init__(self, m, p, l, e, r, s, n):
        self.m = m
        self.p = p
        self.l = l
        self.e = e
        self.r = r
        self.s = s
        self.n = n
        self.eggs = 0

    def run(self):
        for i in range(n):
            self.week()
        return self.m

    def week(self):
        self.egg()
        self.upgradeM()
        self.upgradeP()
        self.upgradeL()
        self.upgradeEgg()

    def egg(self):
        self.eggs += self.m*self.e

    def upgradeL(self):
        self.p = self.l//self.r
        self.l = 0

    def upgradeP(self):
        self.m = self.p//self.s
        self.p = 0
        
    def upgradeM(self):
        self.m = 0

    def upgradeEgg(self):
        self.l = self.eggs
        self.eggs = 0


##try:
    while True:
        inp = input().split()
        m, p, l, e, r, s, n = [int(x) for x in inp]
        eggs = 0
        for i in range(n):
            eggs += m*e
            m = p//s
            p = l//r
            l = eggs
            eggs = 0
        print(m)
##        group = MosquitoGroup(m, p, l, e, r, s, n)
##        print(group.run())
##except:
##    pass
