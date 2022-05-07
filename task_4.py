class Circle:
    def __init__(self, radius: int, x: int = 0, y: int = 0):
        """Х, Y - координаты центра окружности"""
        self.__x = x
        self.__y = y
        self.__radius = radius

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_radius(self):
        return self.__radius

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_radius(self, radius):
        self.__radius = radius

    radius = property(get_radius, set_radius)
    x = property(get_x, set_x)
    y = property(get_y, set_y)

    @staticmethod
    def difference(radius_1, radius_2):
        if radius_1 != radius_2:
            radius = abs(radius_1 - radius_2)
            circle = Circle(radius)
            return circle

        elif radius_1 == radius_2:
            class Point:
                def __init__(self, x=0, y=0):
                    self.__x = x
                    self.__y = y

                def get_x(self):
                    return self.__x

                def set_x(self, x):
                    self.__x = x

                def get_y(self):
                    return self.__y

                def set_y(self, y):
                    self.__y = y

        point = Point()
        return point


circle1 = Circle(5)
circle2 = Circle(5)
result = Circle.difference(circle1.get_radius(), circle2.get_radius())
print(result)
print(result.get_x())
result.set_x(1)
print(result.get_x())
circle3 = Circle(7)
circle4 = Circle(8)
result2 = Circle.difference(circle4.radius, circle3.radius)
print(result2)