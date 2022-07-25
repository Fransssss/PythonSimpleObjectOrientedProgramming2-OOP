class Dog:
    def __init__(self, name, height, weight, life_expectancy, personalities):
        self.name = name
        self.height = height
        self.weight = weight
        self.life_expectancy = life_expectancy
        self.personalities = personalities


    def the_name(self):
        print("The dog's name is " + self.name)

    def the_height(self):
        print("The height of the dog is " + str(self.height) + " inches")

    def the_weight(self):
        print("The weight of the dog is " + str(self.weight) + " pounds")

    def the_life_expectancy(self):
        print("The dog can live for about " + str(self.life_expectancy) + " years")

    def the_personalities(self):
        print("The dog's personalities are " + self.personalities)

    def the_dog_information(self):
        print("\nThe name of the dog is " + self.name)
        print(self.name + "'s height is about " + str(self.height) + " inches")
        print(self.name + "'s weight is about " + str(self.weight) + " pounds")
        print(self.name + " can live for about " + str(self.life_expectancy) + " years")
        print(self.name + " is " + self.personalities)
