import pygame as py
import pygame.freetype as pf

class Saobc:
    def __init__(self, tekst, x, y):
        self.tekst = tekst
        self.kbadrat = py.Rect(x, y, 10, 10)
        self.riso = pf.Font(None, 14)
        self.a = 0

    def ris(self, okno, kamera):
        kbadratnob = py.Rect(self.kbadrat.x + kamera.x , self.kbadrat.y + kamera.y, 10, 10)
        self.riso.render_to(okno, kbadratnob, self.tekst[0:int(self.a)])
        self.a = self.a + 0.2
        
