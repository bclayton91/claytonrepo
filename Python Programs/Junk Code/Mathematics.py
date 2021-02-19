class Math:
    length = 0
    width = 0
    id = ""
    
    def __init__(self,id,l,w):
        self.id = id
        self.length = l
        self.width = w
        
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length*2) + (self.width*2)

rectangle1 = Math("Rectangle",4,5)
square1 = Math("Square",5,5)

Metric1 = [rectangle1.id,rectangle1.length,rectangle1.width,rectangle1.area(),rectangle1.perimeter()]
Metric2 = [square1.id,square1.length,square1.width,square1.area(),square1.perimeter()]
Metrics = [Metric1,Metric2]

print ("The current metrics are:")
print ("  shape length width area perimeter")

for metric in Metrics:
    print (metric)

