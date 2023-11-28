import pygame as py
import seting as se

class Npc:
    def __init__(self,x ,y , kart):
        self.kart = kart
        self.kbadrat = py.Rect(x, y, se.IGROKANOBA, se.IGROKANOBA)
    
    def res(self, okHo, kamera):
        kbadratnob = py.Rect(self.kbadrat.x + kamera.x , self.kbadrat.y + kamera.y, se.IGROKANOBA, se.IGROKANOBA)
        okHo.blit(self.kart, kbadratnob)
