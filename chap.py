class Shape():
    def what_am_i(self):
        print("Я - фигура!")
    


class Rectangle(Shape):
    def __init__(self,a,b):
        self.a1=a
        self.b1=b
    def calculate_perimeter(self):
        return 2*(self.a1+self.b1)

class Square(Shape):
    def __init__(self,a):
        self.a1=a
    def calculate_perimeter(self):
        return self.a1*4
    def change_size(self,a):
        self.a1 += a

rectangle=Rectangle(10,5)
print(rectangle.calculate_perimeter())
rectangle.what_am_i()
    
square=Square(2)
print(square.calculate_perimeter())
square.change_size(2)
print(square.calculate_perimeter())
square.what_am_i()
    


