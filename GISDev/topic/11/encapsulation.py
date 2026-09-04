class Atom:

    def __init__(self, atno, x, y, z):

        self.atno = atno

        self.__position = (x, y, z) #__position is private

    def getPosition(self):

        return self.__position

    def setPosition(self, x, y, z):

        self.__position = (x, y, z)

    def translate(self, x, y, z):

        x0, y0, z0 = self.__position

        self.__position = (x0 + x, y0 + y, z0 + z)



atom = Atom(14, 1, 1, 2)

atom.translate(2, 3, 8)
print (atom.getPosition())