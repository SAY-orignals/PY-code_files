class circle:
    def __init__(self,radius):
        self.radius = radius
    def c_a(self):
        return 3.14*self.radius**2
    def c_c(self):
        return 2*3.14*self.radius
r_c = circle(56)
print("the radius of the circle ",r_c.radius)
print("Area of circle is ",r_c.c_a()," and the circumference is ",r_c.c_c())