class Cat:
    MEOWS = 3

    def meow(self):
        for i in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()