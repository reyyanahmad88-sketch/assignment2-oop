# Start der OOP Aufgabe – wird später erweitert

class Haustier:
    def __init__(self, name, tierart):
        self.name = name
        self.tierart = tierart
        self.hunger = 50
        self.glueck = 50
        self.energie = 50
    def fuettern(self):
        self.hunger -= 20
        if self.hunger < 0:
            self.hunger = 0
        print(f"Mampf mampf! {self.name} hat gefressen und ist zufrieden.")
    def spielen(self):
        self.glueck += 15
        if self.glueck > 100:
            self.glueck = 100

        self.energie -= 10
        if self.energie < 0:
            self.energie = 0

        print(f"{self.name} spielt glücklich herum! 🎾")
    def schlafen(self):
        self.energie += 30
        if self.energie > 100:
            self.energie = 100

        self.hunger += 10
        if self.hunger > 100:
            self.hunger = 100

        print(f"{self.name} hat ein Nickerchen gemacht. 😴")
    def status(self):
        print("------ STATUS ------")
        print(f"Name: {self.name}")
        print(f"Tierart: {self.tierart}")
        print(f"Hunger: {self.hunger}")
        print(f"Glück: {self.glueck}")
        print(f"Energie: {self.energie}")

        if self.hunger < 70 and self.glueck > 30 and self.energie > 20:
            print(f"Es geht {self.name} gut! 😊")
        else:
            print(f"{self.name} braucht vielleicht etwas Aufmerksamkeit!")

        print("--------------------")
    def zustand_pruefen(self):
        if self.hunger > 80:
            print(f"⚠️ Achtung! {self.name} hat sehr großen Hunger!")

        if self.glueck < 30:
            print(f"⚠️ {self.name} fühlt sich einsam oder traurig.")

        if self.energie < 20:
            print(f"⚠️ {self.name} ist sehr müde!")

        if self.hunger <= 80 and self.glueck >= 30 and self.energie >= 20:
            print(f"Alles ist in Ordnung bei {self.name}. 👍")
# Beispiele für die Verwendung der Haustier-Klasse

haustier1 = Haustier("Bello", "Hund")
haustier1.status()
haustier1.spielen()
haustier1.fuettern()
haustier1.status()
haustier1.zustand_pruefen()

print("\n--- Zweites Haustier ---\n")

haustier2 = Haustier("Mimi", "Katze")
haustier2.schlafen()
haustier2.spielen()
haustier2.status()
haustier2.zustand_pruefen()
