class Weapon:
    def __init__(self):
        self.damage = 0

    def fire(self):
        pass


class Pistol(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 10

    def fire(self):
        print("Pew Pew")


class Rifle(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 20

    def fire(self):
        print("Bang Bang")


class Soldier:
    def __init__(self, weapon):
        self.weapon = weapon

    def fireWeapon(self):
        self.weapon.fire()


if __name__ == "__main__":
    soldier = Soldier(Pistol())
    soldier.fireWeapon()

    soldier.weapon = Rifle()
    soldier.fireWeapon()

    soldier.weapon = Weapon()
    soldier.fireWeapon()