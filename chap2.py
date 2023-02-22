class Square():
    square_list = []
    
    def __init__(self,a):
        self.a1=a
        self.square_list.append(self.a1))
        
    def print_size(self):
        print("{} на {} на {} на {}".format(self.a1,self.a1,self.a1,self.a1))

my_square=Square(10)
my_square.print_size()
