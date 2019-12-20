class Circle:
    id = 0
    radius = 0
    color = ""
    display = True 

    def __init__(self,id,r,c,d):
        self.id = id
        self.radius = r
        self.color = c
        self.display = d

    def circumference(self):
        return 3.141 * 2 * self.radius
    
    def area(self):
        return self.radius**2 * 3.141
        


circle1 = Circle(1,10,"Blue",True)
circle2 = Circle(2,8,"yellow",True)
circle3 = Circle(3,17,"red",False)

stats_1 = (circle1.id, circle1.color,circle1.circumference(), circle1.area())
stats_2 = (circle2.id, circle2.color,circle2.circumference(), circle2.area())
stats_3 = (circle3.id, circle3.color,circle3.circumference(), circle3.area())

stats = [stats_1, stats_2, stats_3]

print ("id, color, circumference, area")
for circles in stats:
    print (circles)