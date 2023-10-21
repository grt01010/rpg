import pygame as py

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

    def podelit_kartinki(self):
        for y in range(0, 8):
            for x in range(0, 17):
                kart = self.kartinka.subsurface(x * 16, y * 16, 16, 16)
                self.spisok_kartinok.append(kart)

    def sozdanie_plitok(self):
        for y in range(0, len(self.spisokcsv)):
            for x in range(0, len(self.spisokcsv[y])):
                nomer = int(self.spisokcsv[y][x])
                plitka = Plitka(self.spisok_kartinok[nomer], x * 16, y * 16, nomer)
                self.plitki.append(plitka)

    def res(self, okHo):
        for plitka in self.plitki:
            plitka.res(okHo)
                

class Plitka:
    def __init__(self, kart, x, y, nomer):
        self.kartinka = kart
        self.kbadrat = py.Rect(x, y, 16, 16)
        self.nomer = nomer

    def res(self, okHo):
        okHo.blit(self.kartinka, self.kbadrat)
