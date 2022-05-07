"""Домашнее задание, пункт номер 1"""


class Triangle:

    def __init__(self, a, b, c):
        if self.check(a, b, c):
            self.__a = a
            self.__b = b
            self.__c = c
            print('The triangle was created!')
        else:
            raise TypeError('Unappropriate values.')

    def get_first_side(self):
        return self.__a

    def get_second_side(self):
        return self.__b

    def get_third_side(self):
        return self.__c    

    def set_first_side(self, side):
        if self.check(side, self.__b, self.__c):
            print("The side's value was changed.")
            self.__a = side
        else:
            raise TypeError('Unappropriate values.')
    
    def set_second_side(self, side):
        if self.check(side, self.__a, self.__c):
            self.__b = side
            print("The side's value was changed.")
        else:
            raise TypeError('Unappropriate values.')
    
    def set_third_side(self, side):
        if self.check(side, self.__a, self.__b):
            print("The side's value was changed.")
            self.__c = side
        else:
            raise TypeError('Unappropriate values.')

    def delete_first_side(self):
        print("The side's value was deleted.")
        del self.__a

    def delete_second_side(self):
        print("The side's value was deleted.")
        del self.__b

    def delete_third_side(self):
        print("The side's value was deleted.")
        del self.__c

    a = property(get_first_side, set_first_side, delete_first_side)
    b = property(get_second_side, set_second_side, delete_second_side)
    c = property(get_third_side, set_third_side, delete_third_side)

    @staticmethod
    def check(a, b, c):
        """According to the rules of metamatics, 
        a triangle can exist only if any of its sides is 
        less than the sum of the lengths of its other two sides."""
        if a < b + c:
            return True
        
        else:
            return False


tr1 = Triangle(5, 4, 10)
tr1.a = 10
del tr1.a
tr1.a = 12
