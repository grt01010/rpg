import pygame as py
import seting as se

class Karta:
    def __init__(self):
        self.kartinka = py.image.load('rpg_tileset.png')
        self.spisokcsv = []
        d = open('karta..csv', 'r')
        for i in d:
            ai = i.split(',')
            self.spisokcsv.append(ai)
        self.spisok_kartinok = []
        self.podelit_kartinki()
        self.plitki = []
        self.sozdanie_plitok()
        self.shir = len(self.spisokcsv[0])*se.PLITKANOBA



    def podelit_kartinki(self):
        for y in range(0, 8):
            for x in range(0, 17):
                kart = self.kartinka.subsurface(x * se.PLITKASTARA, y * se.PLITKASTARA, se.PLITKASTARA, se.PLITKASTARA)
                kart = py.transform.scale(kart,[se.PLITKANOBA, se.PLITKANOBA])
                self.spisok_kartinok.append(kart)

    def sozdanie_plitok(self):
        for y in range(0, len(self.spisokcsv)):
            for x in range(0, len(self.spisokcsv[y])):
                nomer = int(self.spisokcsv[y][x])
                plitka = Plitka(self.spisok_kartinok[nomer], x * se.PLITKANOBA, y * se.PLITKANOBA, nomer)
                self.plitki.append(plitka)

    def res(self, okHo, kamera):
        for plitka in self.plitki:
            plitka.res(okHo, kamera)
                

class Plitka:
    def __init__(self, kart, x, y, nomer):
        self.kartinka = kart
        self.kbadrat = py.Rect(x, y, se.PLITKANOBA, se.PLITKANOBA)
        self.nomer = nomer

    def res(self, okHo, kamera):
        kbadratnob = py.Rect(self.kbadrat.x + kamera.x , self.kbadrat.y + kamera.y, se.PLITKANOBA, se.PLITKANOBA)
        okHo.blit(self.kartinka, kbadratnob)


