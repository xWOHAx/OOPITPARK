
class Fish:
    def __init__(self, name, color, size, speed):
        self.name = name
        self.color = color
        self.size = size
        self.speed = speed
        self.hunger = 0

    def swim(self):
        print(f"{self.name} плывет со скоростью {self.speed}.")

    def feed(self):
        print(f"{self.name} накормлена.")
        self.hunger = 0

    def Hunger(self):
        self.hunger += 1
        print(f"{self.name} голоден.")


class Goldfish(Fish):
    def __init__(self, name):
        super().__init__(name, "золотой", "небольшая", "медленная")


class Shark(Fish):
    def __init__(self, name):
        super().__init__(name, "серый", "крупная", "быстрая")


class Clownfish(Fish):
    def __init__(self, name):
        super().__init__(name, "яркий", "среднего размера", "средняя")


class Aquarium:
    def __init__(self):
        self.fishes = []

    def add_fish(self, fish):
        self.fishes.append(fish)
        print(f"{fish.name} добавлена в аквариум.")

    def remove_fish(self, fish):
        if fish in self.fishes:
            self.fishes.remove(fish)
            print(f"{fish.name} удалена из аквариума.")
        else:
            print(f"{fish.name} не найдена в аквариуме.")

    def watch(self):
        print("Все рыбки в аквариуме:")
        for fish in self.fishes:
            fish.swim()

    def feed(self):
        print("Рыбки накормлены:")
        for fish in self.fishes:
            fish.feed()


if __name__ == "__main__":
    aquarium = Aquarium()

    goldfish = Goldfish("Золотая рыбка")
    shark = Shark("Акула")
    clownfish = Clownfish("Рыбка-клоун")

    aquarium.add_fish(goldfish)
    aquarium.add_fish(shark)
    aquarium.add_fish(clownfish)

    aquarium.watch()


    for _ in range(3):
        for fish in aquarium.fishes:
            fish.Hunger()

    aquarium.feed()
    aquarium.watch()