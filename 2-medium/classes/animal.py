class Animal:
    def __init__(self, size, species):
        self.size = size
        self.species = species

    def sizeCheck(self):
        if self.size != "small":
            if self.size != "medium":
                if self.size != "large":
                    return "Enter either: small, medium, large"
        return self.size

    def amdog(self):
        if self.species == "dog":
            return "Woof"
        return "you are not a dog"
