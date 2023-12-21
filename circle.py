import math


def area(r):
    """
    Принимает радиус r круга и возвращает его площать

        :param r: (int/float) радиус круга
        :return: (float) площадь круга радиуса r
    """
    return math.pi * r * r


def perimeter(r):
    """
    Принимает радиус r круга и возвращает его длину окружности

        й:param r: (int/float) радиус круга
        :return: (float) длина окружности круга с радиусом r
    """
    return 2 * math.pi * r

