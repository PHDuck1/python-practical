class Washing:

    @staticmethod
    def wash():
        print("Washing...")


class Rinsing:

    @staticmethod
    def rinse():
        print("Rinsing...")


class Spinning:

    @staticmethod
    def spin():
        print("Spinning...")


class WashingMachine:
    
    @staticmethod
    def startWashing():
        Washing().wash()
        Rinsing().rinse()
        Spinning().spin()
