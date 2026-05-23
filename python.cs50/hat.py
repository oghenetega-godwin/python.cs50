import random


class Hat:
        houses = ["Godwin", "Ofuyaekpone", "Sunday"]
    

        @classmethod
        def sort(cls, name):
            print(name, "is in house", random.choice(cls.houses))



Hat.sort("Tega")