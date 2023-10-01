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


# Создаем список объектов Car
car1 = Car(1, "Toyota", "Camry", 2019, "Синий", 25000, "AB123CD")
car2 = Car(2, "Ford", "Focus", 2017, "Красный", 18000, "EF456GH")
car3 = Car(3, "Honda", "Civic", 2020, "Белый", 27000, "IJ789KL")
car4 = Car(4, "Toyota", "Corolla", 2015, "Черный", 20000, "MN012OP")
car5 = Car(5, "Ford", "Mustang", 2018, "Желтый", 35000, "QR345ST")

cars = [car1, car2, car3, car4, car5]


# Функция для вывода списка автомобилей заданной марки
def get_cars_by_brand(cars_list, brand):
    return [car for car in cars_list if car.brand == brand]


# Функция для вывода списка автомобилей заданной модели, которые эксплуатируются больше n лет
def get_cars_by_model_and_age(cars_list, model, n, current_year):
    return [car for car in cars_list if car.model == model and car.get_age(current_year) > n]


# Вывод списка автомобилей заданной марки
brand_to_search = "Toyota"
brand_cars = get_cars_by_brand(cars, brand_to_search)
print(f"Список автомобилей марки {brand_to_search}:")
for car in brand_cars:
    print(car.display_info())

# Вывод списка автомобилей заданной модели, которые эксплуатируются больше n лет
model_to_search = "Focus"
years_to_compare = 3
current_year = 2023
model_cars = get_cars_by_model_and_age(cars, model_to_search, years_to_compare, current_year)
print(f"\nСписок автомобилей модели {model_to_search}, которые эксплуатируются больше {years_to_compare} лет:")
for car in model_cars:
    print(car.display_info())
