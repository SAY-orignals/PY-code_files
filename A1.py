class rectangle:
    def __init__(self,w,l):
        self.length = l
        self.width = w
    def rect_a(self):
        return self.length*self.width 
drect  = rectangle(45,48)
print("Dimension of the rectangle is: Length:",drect.length,", Width:",drect.width)
print("Area of the rectangle is :",drect.rect_a())