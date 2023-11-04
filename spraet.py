import pygame as py
import seting as se

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
            e = self.s.subsurface(a, 0, se.IGROKSTARA, se.IGROKSTARA)
            a = a + 32
            e = py.transform.scale(e,[se.IGROKANOBA, se.IGROKANOBA])
            self.BHuc.append(e)
        for dota in range(4):
            e = self.s.subsurface(a2, 32, se.IGROKSTARA, se.IGROKSTARA)
            a2 = a2 + 32
            e = py.transform.scale(e,[se.IGROKANOBA, se.IGROKANOBA])
            self.BleBo.append(e)
        for dota in range(4):
            e = self.s.subsurface(a3, 64, se.IGROKSTARA, se.IGROKSTARA)
            a3 = a3 + 32
            e = py.transform.scale(e,[se.IGROKANOBA, se.IGROKANOBA])
            self.BnraBo.append(e)
        for dota in range(4):
            e = self.s.subsurface(a4, 96, se.IGROKSTARA, se.IGROKSTARA)
            a4 = a4 + 32
            e = py.transform.scale(e,[se.IGROKANOBA, se.IGROKANOBA])
            self.Berx.append(e)
        self.kbadrat = py.Rect(100, 20, se.IGROKANOBA, se.IGROKANOBA)
        self.tek = self.BHuc

    
    def res(self, okHo, kamera):
        kbadratnob = py.Rect(self.kbadrat.x + kamera.x , self.kbadrat.y + kamera.y, se.IGROKANOBA, se.IGROKANOBA)
        okHo.blit(self.tek[self.ahem], kbadratnob)



    def dBio(self):
        ran = py.key.get_pressed()
        self.y = 0
        self.x = 0
        if ran[py.K_s] == True:
            self.y = 5
            self.tek = self.BHuc
            self.ahem = self.ahem + 1
        elif ran[py.K_a] == True:
            self.x = -5
            self.tek = self.BleBo
            self.ahem = self.ahem + 1
        elif ran[py.K_w] == True:
            self.y = -5
            self.ahem = self.ahem + 1
            self.tek = self.Berx
        elif ran[py.K_d] == True:
            self.x = 5
            self.tek = self.BnraBo
            self.ahem = self.ahem + 1
        elif ran[py.K_z] == True:
            a = open('zzz', 'w')
            a.write(str(self.kbadrat.x)+', '+str(self.kbadrat.y))
            a.close()
        self.kbadrat.y = self.kbadrat.y + self.y
        self.kbadrat.x = self.kbadrat.x + self.x
        if self.ahem == 4:
                self.ahem = 0