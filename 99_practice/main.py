import abc

class Shape():
    __metaClass__ = abc.ABCMeta

    def __init__(self, *dimensions):
        self.dimensions = dimensions

    @abc.abstractmethod
    def getArea():
        pass

class Triangle(Shape):
    def __init__(self, *dimensions):
        super().__init__(dimensions)
        self.dimensions = dimensions

    @property
    def area(self):
        return self.dimensions[0] * self.dimensions[1] / 2


class Square(Shape):
    def __init__(self, *dimensions):
        super().__init__(dimensions)
        self.dimensions = dimensions

    @property
    def area(self):
        return self.dimensions[0] * self.dimensions[1]

t = Triangle(5, 10)
print(t.area)

s = Square(12, 45)
print(s.area)
