import pygame as py

class Ads:
    def __init__(self,x,y,xr,yr):
        self.x=x
        self.y=y
        self.x=xr
        self.y=yr
        self.pober = py.surface.Surface([xr,yr], py.SRCALPHA)
        self.ads=255