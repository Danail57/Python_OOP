from typing import ClassVar


class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: ClassVar[float] = 1.25
    fuel_consumption: float
    fuel: float
    capacity: float
    horse_power: float

    def __init__(self, fuel: float, horse_power: float):
        self.fuel = fuel
        self.capacity = self.fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        fuel_needed = self.fuel_consumption * kilometers
        if self.fuel < fuel_needed:
            raise Exception("Not enough fuel")
        self.fuel -= fuel_needed

    def refuel(self, fuel):
        if self.fuel + fuel > self.capacity:
            raise Exception("Too much fuel")
        self.fuel += fuel

    def __str__(self):
        return f"The vehicle has {self.horse_power} " \
               f"horse power with {self.fuel} fuel left and {self.fuel_consumption} fuel consumption"



from unittest import TestCase, main

class TestVehicle(TestCase):
    fuel = 4.5
    horse_power = 112.5

    def setUp(self):
        self.test_vehicle = Vehicle(self.fuel, self.horse_power)

    def test_class_attributes_types(self):
        self.assertIsInstance(self.test_vehicle.DEFAULT_FUEL_CONSUMPTION, float)
        self.assertIsInstance(self.test_vehicle.fuel, float)
        self.assertIsInstance(self.test_vehicle.capacity, float)
        self.assertIsInstance(self.test_vehicle.horse_power, float)
        self.assertIsInstance(self.test_vehicle.fuel_consumption, float)

    def test_init(self):
        self.assertEqual(self.fuel, self.test_vehicle.fuel)
        self.assertEqual(self.fuel, self.test_vehicle.capacity)
        self.assertEqual(self.horse_power, self.test_vehicle.horse_power)
        self.assertEqual(1.25, self.test_vehicle.fuel_consumption)

    def test_drive_success(self):
        self.test_vehicle.drive(2)
        self.assertEqual(2, self.test_vehicle.fuel)

    def test_drive_error(self):
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.drive(5)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_success(self):
        self.test_vehicle.fuel = 1
        self.test_vehicle.refuel(2.3)
        self.assertEqual(3.3, self.test_vehicle.fuel)

    def test_refuel_error(self):
        self.test_vehicle.fuel = 1
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.refuel(8.5)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_string(self):
        self.test_vehicle.fuel = 1.75
        expected = f"The vehicle has 112.5 horse power with 1.75 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected, str(self.test_vehicle))

if __name__ == "__main__":
    main()
