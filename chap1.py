class Horse():
    def __init__(self,name,color,owner):
        self.name=name
        self.color=color
        self.owner=owner

class Person():
    def __init__(self,name):
        self.name=name
        
agir=Person("Agir")
flame=Horse("Flame","black",agir)

print(flame.owner.name,"on",flame.name)
