#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, color="", size=5, material="", condition=""):
        self.brand = brand
        self.color = color
        self.size = size
        self.material = material
        self.condition = condition

    def cobble(self, condition="new"):
        self.condition = "New"
        print(f"Your shoe is as good as {condition}!")

    def get_size(self):
        print("Retrieving size")
        return self._size

    def set_size(self, size):
        if (type(size) == int):
            self._size = size
            print(f"Setting size to {size}.")
        else:
            print("size must be an integer")

    size = property(get_size, set_size)

adidas = Shoe("Adidas", "Red", 5, "Leather", "Used")
nike = Shoe("Nike", "White", "", "Canvas", "Used")