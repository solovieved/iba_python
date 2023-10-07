import unittest
from lab5.Car import Car


class TestCarMethods(unittest.TestCase):
    def setUp(self):
        self.car1 = Car(1, "Toyota", "Camry", 2020, "Синий", 25000, "AB123456")
        self.car2 = Car(2, "Honda", "Civic", 2020, "Серебристый", 22000, "CD789012")
        self.car3 = Car(3, "Ford", "Focus", 2021, "Красный", 28000, "EF345678")

    def test_get_age(self):
        current_year = 2023
        self.assertEqual(self.car1.get_age(current_year), 3)
        self.assertEqual(self.car2.get_age(current_year), 3)
        self.assertEqual(self.car3.get_age(current_year), 2)

    def test_is_valid_registration_number(self):
        self.assertTrue(Car.is_valid_registration_number("AB123456"))
        self.assertTrue(Car.is_valid_registration_number("CD789012"))
        self.assertFalse(Car.is_valid_registration_number("1234"))

    def test_car_comparison(self):
        self.assertTrue(self.car1 < self.car3)
        self.assertTrue(self.car2 <= self.car2)
        self.assertTrue(self.car1 == Car(1, "Toyota", "Camry", 2020, "Синий", 25000, "AB123456"))
        self.assertFalse(self.car2 == self.car3)


if __name__ == '__main__':
    unittest.main()