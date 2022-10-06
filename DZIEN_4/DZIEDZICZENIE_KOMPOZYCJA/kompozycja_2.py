class Component:

    def __init__(self):
        print("Element składowy ABC")

    def opercjaA(self):
        print("wykonanie pierwszej operacji przez klasę Component...")

class Composite:

    def __init__(self):
        self.element1 = Component()
        print("Kompozyt zostaał utworzony na bazie Component")

    def operacjaAB(self):
        print("wykonanie pierwszej operacji przez klasę Compozyt...")
        self.element1.opercjaA()

cmp = Composite()

cmp.operacjaAB()
#cmp.operacjaA()
