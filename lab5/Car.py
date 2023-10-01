class Car:
    def __init__(self, car_id, brand, model, year, color, price, registration_number):
        self.__car_id = car_id  # Используем инкапсуляцию для car_id
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__color = color
        self.__price = price
        self.__registration_number = registration_number

    @property
    def car_id(self):
        return self.__car_id

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str):
            self.__brand = brand
        else:
            print("Ошибка: Марка должна быть строкой.")

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if isinstance(model, str):
            self.__model = model
        else:
            print("Ошибка: Модель должна быть строкой.")

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if isinstance(year, int) and year > 0:
            self.__year = year
        else:
            print("Ошибка: Год выпуска должен быть положительным целым числом.")

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if isinstance(color, str):
            self.__color = color
        else:
            print("Ошибка: Цвет должен быть строкой.")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if isinstance(price, (int, float)) and price >= 0:
            self.__price = price
        else:
            print("Ошибка: Цена должна быть неотрицательным числом.")

    @property
    def registration_number(self):
        return self.__registration_number

    @registration_number.setter
    def registration_number(self, new_registration_number):
        if isinstance(new_registration_number, str) and len(new_registration_number) == 8:
            self.__registration_number = new_registration_number
        else:
            print("Ошибка: Регистрационный номер должен быть строкой из 8 символов.")

    def get_age(self, current_year):
        return current_year - self.year

    @staticmethod
    def is_valid_registration_number(registration_number):
        return len(registration_number) == 8

    def display_info(self):
        return f"ID: {self.car_id}, Марка: {self.brand}, Модель: {self.model}, Год выпуска: {self.year}, Цвет: {self.color}, Цена: {self.price}, Регистрационный номер: {self.registration_number}"

    def __str__(self):
        return f"Марка: {self.brand}, Модель: {self.model}, Год выпуска: {self.year}, Цвет: {self.color}"

    def __eq__(self, other):
        if isinstance(other, Car):
            return self.car_id == other.car_id
        return False

    def __lt__(self, other):
        if isinstance(other, Car):
            return self.year < other.year
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Car):
            return self.year <= other.year
        return NotImplemented

    def __hash__(self):
        return hash(self.car_id)


car1 = Car(1, "Toyota", "Camry", 2020, "Синий", 25000, "AB123456")
car2 = Car(2, "Honda", "Civic", 2020, "Серебристый", 22000, "CD789012")
car3 = Car(3, "Toyota", "Camry", 2020, "Синий", 25000, "EF345678")

# __str__
print(str(car1))

# __eq__
print(car1 == car2)
print(car1 == car3)

# __lt__
print(car1 < car2)

# __le__
print(car1 <= car2)
print(car1 <= car3)

# __hash__
car_set = {car1, car2}
print(len(car_set))