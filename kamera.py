class Kamera:
    def __init__(self, igrok):
        self.igrok = igrok
        self.x = 0
        self.y = 0
    def cle (self):
        self.x = self.igrok.kbadrat.x * -1
        self.y = self.igrok.kbadrat.y * -1
