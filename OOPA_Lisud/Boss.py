from Swordsman import Swordsman
from Archer import Archer
from Mage import Mage

class Boss(Swordsman, Archer, Mage):
    def __init__(self, username):
        super().__init__(username)
        self.setStr(10)
        self.setVit(25)
        self.setInt(5)
        self.setHp(self.getHp()+self.getVit())
        