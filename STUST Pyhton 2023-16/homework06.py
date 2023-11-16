class MyShape:
    def __init__(self, square_side , length,width,radius):
        self.square_side=square_side
        self.length=length
        self.width=width
        self.radius=radius
    def Count_Square(self):
        return f"Square={self.square_side * self.square_side}"
    def Count_retangle(self):
        return f"retangle={self.width * self.length}"
    def Count_circle(self):
        return f"circle={self.radius * self.radius *3.14}"
value = MyShape(5,4,3,3)
print (value.Count_Square())
print (value.Count_retangle())
print (value.Count_circle())
