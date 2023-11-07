import seting as se

class Kamera:
    def __init__(self, igrok):
        self.igrok = igrok
        self.x = 0
        self.y = 0
    def cle (self):
        self.x = self.igrok.kbadrat.x * -1 + se.RACMERX / 2
        self.y = self.igrok.kbadrat.y * -1 + se.RACMERY / 2
        if self.igrok.kbadrat.x < se.RACMERX / 2:
            self.x = 0
        if self.igrok.kbadrat.y < se.RACMERY / 2:
            self.y = 0
        
        
