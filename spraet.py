import pygame as py

class xtk:
    def __init__(self):
        self.s = py.image.load('xtk.png')
        self.BHuc = []
        self.BleBo = []
        self.BnraBo = []
        self.Berx = []
        self.x = 0
        self.y = 0
        a = 0
        a2 = 0
        a3 = 0
        a4 = 0
        self.ahem = 0
        for dota in range(4):
            e = self.s.subsurface(a, 0, 32, 32)
            a = a + 32
            self.BHuc.append(e)
        for dota in range(4):
            e = self.s.subsurface(a2, 32, 32, 32)
            a2 = a2 + 32
            self.BleBo.append(e)
        for dota in range(4):
            e = self.s.subsurface(a3, 64, 32, 32)
            a3 = a3 + 32
            self.BnraBo.append(e)
        for dota in range(4):
            e = self.s.subsurface(a4, 96, 32, 32)
            a4 = a4 + 32
            self.Berx.append(e)
        self.kbadrat = py.Rect(100, 20, 32, 32)
        self.tek = self.BHuc

    
    def res(self, okHo):
        okHo.blit(self.tek[self.ahem], self.kbadrat)

    def dBio(self):
        ran = py.key.get_pressed()
        self.y = 0
        self.x = 0
        if ran[py.K_s] == True:
            self.y = 1
            self.tek = self.BHuc
            self.ahem = self.ahem + 1
        elif ran[py.K_a] == True:
            self.x = -1
            self.tek = self.BleBo
            self.ahem = self.ahem + 1
        elif ran[py.K_w] == True:
            self.y = -1
            self.ahem = self.ahem + 1
            self.tek = self.Berx
        elif ran[py.K_d] == True:
            self.x = 1
            self.tek = self.BnraBo
            self.ahem = self.ahem + 1
        self.kbadrat.y = self.kbadrat.y + self.y
        self.kbadrat.x = self.kbadrat.x + self.x
        if self.ahem == 4:
                self.ahem = 0