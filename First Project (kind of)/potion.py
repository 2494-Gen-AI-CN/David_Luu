import time

class Potion:
    def __init__(self, name, effect, number):
        self.name = name
        self.effect = effect
        self.number = number

    def use(self):
        if self.number > 0:
            self.number -= 1
            print(f"You used the {self.name}. {self.effect}")
            time.sleep(1)
            return
        else:
            print(f"You are out of {self.name}s.")
            time.sleep(1)
            return