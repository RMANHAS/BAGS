class polygon:
    __width = None
    __height = None

    def set_value(self, width, height):
        self.__weidht = width
        self.__height = height

    def get_widht(self):
        return self.__width

    def get_height(self):
        return self.__height


class square(polygon):
    def area(self):
        return self.get_widht() * self.get_height()


class triangle(polygon):
    def area(self):
        return self.get_weidht() * self.get_height()


s1 = square()
s1.set_value(2, 30)
print(s1.area())

s2 = triangle()
s2.set_value(2, 3)
print(s2.area())
