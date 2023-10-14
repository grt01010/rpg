import pygame as py

class Karta:
    def __init__(self):
        self.kartinka = py.image.load('rpg_tileset.png')
        self.spisokcsv = []
        d = open('karta..csv', 'r')
        for i in d:
            ai = i.split(',')
            self.spisokcsv.append(ai)