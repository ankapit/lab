import doctest


# TODO Написать 3 класса с документацией и аннотацией типов
class HandmadeJewelry:
    def __init__(self, length: float, num_beads: int, clasp: bool):
        """
        Создание и подготовка к работе объекта "Украшение ручной работы"

        :param length: Длина украшения в см
        :param num_beads: Количество бусин в изделии
        :param clasp: Наличие застежки

        Примеры:
        >>> bracelet = HandmadeJewelry(34, 60, True)  # инициализация экземпляра класса
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина украшения int или float")
        if length <= 0:
            raise ValueError("Длина украшения должна быть положительным числом")
        self.length = length

        if not isinstance(num_beads, int):
            raise TypeError("Количество бусин int")
        if num_beads <= 0:
            raise ValueError("Количество бусин должно быть положительным числом")
        self.num_beads = num_beads

        if not isinstance(clasp, bool):
            raise TypeError("Наличие застежки должно быть bool ")
        self.clasp = clasp

    def availability_of_clasp(self) -> bool:
        """
        Функция которая проверяет есть ли застежки в украшении

        :return: есть ли застежки в украшении

        Примеры:
        >>> bracelet1 = HandmadeJewelry(34, 60, False)
        >>> bracelet1.availability_of_clasp()
        """
        ...

    def add_clasp(self) -> None:
        """
        Добавление застежки в изделие.

        Примеры:
        >>> bracelet = HandmadeJewelry(34, 60, False)
        >>> bracelet.add_clasp()
        """

        ...

    def change_in_length(self, desired_length: float) -> int:
        """
        Изменение длины изделия.

        :param desired_length: Желаемая длина
        :raise ValueError: Если желаемая длина < 0,то возвращается ошибка.

        :return: Количество бусин, необходимое для покрытия желаемой длины изделия

        Примеры:
        >>> bracelet = HandmadeJewelry(34, 60, False)
        >>> bracelet.change_in_length(50)
        """


class Meal:
    def __init__(self, meat: float, vegetables: float, spice: bool):
        """
        Создание и подготовка к работе объекта "Блюдо"

        :param meat: мясо в граммах, входящее в состав блюда
        :param vegetables: овощи в граммах, входящее в состав блюда
        :param spice: наличие специй

        Примеры:
        >>> soup = Meal(34, 60, True)  # инициализация экземпляра класса
        """
        if not isinstance(meat, (int, float)):
            raise TypeError("мясо в граммах int или float")
        if meat < 0:
            raise ValueError("мясо в граммах должно быть неотрицательным числом")
        self.meat = meat

        if not isinstance(vegetables, (int, float)):
            raise TypeError("овощи в граммах int или float")
        if vegetables <= 0:
            raise ValueError("овощи в граммах должны быть неотрицательным числом")
        self.vegetables = vegetables

        if not isinstance(spice, bool):
            raise TypeError("наличие специй должно быть bool")
        self.spice = spice

    def vegetarian_dish(self) -> bool:
        """
        Функция которая проверяет есть ли мясо в блюде

        :return: есть ли мясо в блюде

        Примеры:
        >>> soup = Meal(70, 60, False)
        >>> soup.vegetarian_dish()
        """
        ...

    def add_vegetables(self, num_vegetables: float) -> None:
        """
        Добавление овощей в блюдо.
        :param num_vegetables: желаемое количество грамм овощей в блюде

        Примеры:
        >>> soup = Meal(34, 60, True)
        >>> soup.add_vegetables(200)
        """
        if not isinstance(num_vegetables, (int,float)):
            raise TypeError("вес добавляемых овощей должно быть int или float")

class Garland:
    def __init__(self, light_num: int, color: str, turn_on: bool):
        """
        Создание и подготовка к работе объекта "Гирлянда"

        :param light_num: количество лампочек
        :param color: цвет гирлянды
        :param turn_on: включена она или выключена

        Примеры:
        >>> garland1 = Garland(10, "green", True)  # инициализация экземпляра класса
        """
        if not isinstance(light_num, int):
            raise TypeError("количество лампочек int ")
        if light_num <= 0:
            raise ValueError("количество лампочек должно быть положительным числом")
        self.light_num = light_num

        if not isinstance(color, str):
            raise TypeError("Цвет гирлянды str ")
        self.color = color

        if not isinstance(turn_on, bool):
            raise TypeError("Гирлянда либо включена, либо нет")
        self.turn_on = turn_on

    def add_light(self, light_num: int) -> int:
        """
        Функция которая добавляет в гирлянду лампочки

        :return: новое количество лампочек

        Примеры:
        >>> garland1 = Garland(10, "green", True)
        >>> garland1.add_light(5)
        """
        if not isinstance(light_num, int):
            raise TypeError("Количество добавляемых лампочек должно быть int ")


    def check_light(self) -> bool:
        """
        Функция проверяет включена ли гирлянда

        :return: включена ли гирлянда

        Примеры:
        >>> garland1 = Garland(15, "green", True)
        >>> garland1.check_light()
        """


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
