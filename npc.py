import pygame as py
import seting as se
import caob as ca

class Npc:
    def __init__(self, x, y, kart):
        self.kart = kart
        self.kbadrat = py.Rect(x, y, se.IGROKANOBA, se.IGROKANOBA)
        self.saob=ca.Saobc('zzzzzz', x, y)
        self.radom = 0
        self.x = x
        self.y = y
        self.ck = 3
    
    def res(self, okHo, kamera):
        kbadratnob = py.Rect(self.kbadrat.x + kamera.x , self.kbadrat.y + kamera.y, se.IGROKANOBA, se.IGROKANOBA)
        okHo.blit(self.kart, kbadratnob)
        if self.radom == 1:
            self.saob.ris(okHo, kamera)

    def dbig(self, igrok):
        a = igrok.kbadrat.x - self.kbadrat.x
        b = igrok.kbadrat.y - self.kbadrat.y
        c = ((a*a)+(b*b))**0.5
        sint = a/c
        cost = b/c
        skx = sint*self.ck
        sky = cost*self.ck
        if abs(igrok.kbadrat.x-self.kbadrat.x)<50 and abs(igrok.kbadrat.y-self.kbadrat.y)<50:
            self.radom = 1
        else:
            self.radom = 0
            self.saob.a = 0
        self.saob.kbadrat.x = self.kbadrat.x
        self.saob.kbadrat.y = self.kbadrat.y
        if self.radom == 0:
            self.kbadrat.x=self.kbadrat.x+skx
            self.kbadrat.y=self.kbadrat.y+sky
        
        

