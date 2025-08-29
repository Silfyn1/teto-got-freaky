class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def present(self):
        print("Meu nome eh " + self.name)
        print("Eu tenho " + str(self.age) + " anos")

# Como criar um objeto dessa classe ----------------
    
# Toda vez que eu chamo Animal() ele chama o __init__(self)

pessoas = [Animal("silfyn uwu", 21), Animal("sofia uwu", 23)]

for pessoa in pessoas:
    pessoa.present()