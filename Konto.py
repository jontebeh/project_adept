class konto(object):
    def __init__(self, inhaber, kontonummer, pin, kontostand, kontokorrent = 0):
        self.Inhaber = inhaber
        self.Kontonummer = kontonummer
        self.Pin = pin
        self.Kontostand = kontostand
        self.Konotkorrent = kontokorrent
        
    def ueberweisen(self, ziel, betrag):
        if self.Kontostand - betrag < -self.Konotkorrent:
            return False
        else:
            self.Kontostand -= betrag
            ziel.Kontostand += betrag
            return True
        
    def einzahlen(self, betrag):
        self.Kontostand += betrag
        return True
    
    def auszahlen(self, betrag):
        if self.Kontostand - betrag < -self.Konotkorrent:
            return False
        else:
            self.Kontostand -= betrag
        
    def kontostand(self):
        return self.Kontostand