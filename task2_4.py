if __name__ == "__main__":
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

            :return: Является ли блюдо вегетарианским

            Примеры:
            >>> stew = Meal(70, 60, False)
            >>> stew.vegetarian_dish()
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
            if not isinstance(num_vegetables, (int, float)):
                raise TypeError("вес добавляемых овощей должно быть int или float")

        def __str__(self):
            return f"Вес блюда: {self.meat + self.vegetables} граммов." \
                   f" Наличие специй в блюде: {self.spice}"

        def __repr__(self):
            return f"{self.__class__.__name__}({self.meat!r}, {self.vegetables!r}, {self.spice!r})"


    class Soup(Meal):
        def __init__(self, meat: float, vegetables: float, spice: bool, broth: str):
            """
                        Перегружаем init.
                        :param broth: Вес бульона
                        Добавили тип бульона, так как объект из класса Meal
                        может не требовать добавления жидкости (например, десерт).

                        Чтобы суп был вкусным, он должен содержать приправы
                        :raise ValueError: Если суп не содержит приправ, то вызываем ошибку

                        """
            super().__init__(meat, vegetables, spice)
            if not spice:
                raise ValueError("Суп должен содержать специи")
            self.spice = spice
            self.broth = broth

        def __repr__(self):
            """
            Перегружаем repr.
            Добавили вывод веса бульона.
            """
            return f"{self.__class__.__name__}({self.meat!r}, {self.vegetables!r}, {self.spice!r}, {self.broth!r})"

        """
        Метод add_vegetables просто наследуем.
        """
        def __str__(self):
            """
            Перегружаем str.
            Уточнили что вес мяса и овощей теперь не равен весу блюда.
            """
            return f"Вес твердых ингредиентов: {self.meat + self.vegetables} граммов." \
                   f" Наличие специй в блюде: {self.spice}"


        def vegetarian_dish(meat, broth):
            """
            Перегружаем метод vegetarian_dish.

            Чтобы суп был вегетарианским, он не должен содержать мясо и должен быть на овощном бульоне.
            Добавляем условие на то, что бульон должен быть овощным.

            :return: Является ли блюдо вегетарианским с учетом входящего в состав бульона
            """

            return (meat == 0) and broth == "Овощной"

    stew = Meal(100, 200, True)
    print(stew)
    Cheese_soup = Soup(0, 200, True, "Овощной")
    print(Cheese_soup)


    pass
