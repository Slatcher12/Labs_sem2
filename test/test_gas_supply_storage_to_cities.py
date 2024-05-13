
import unittest
from src.gas_supply_storage_to_cities import get_unreachable_cities_for_supply


class TestGetUnreachableCitiesForSupply(unittest.TestCase):
    def test_normal_input(self):
        get_unreachable_cities_for_supply('gas_supply_storage_to_cities_input.txt', 'gas_supply_storage_to_cities_output.txt')
        with open(
            "../resources/gas_supply_storage_to_cities_output.txt",
            'r',
            encoding='utf-8'
        ) as file:
            first_line = file.readline()
            second_line = file.readline()
        self.assertEqual(first_line, "('kyiv', ['lviv', 'sudova-vyshnia', 'zhovkva', 'busk'])\n")
        self.assertEqual(second_line, "('sudova-vyshnia', ['kyiv', 'lviv'])\n")

    def test_supply_to_all_cities(self):
        get_unreachable_cities_for_supply('gas_supply_storage_to_cities_input.txt', 'gas_supply_storage_to_cities_output.txt')
        with open(
            "../resources/gas_supply_storage_to_cities_output.txt",
            'r',
            encoding='utf-8'
        ) as file:
            first_line = file.readline()
        self.assertEqual(first_line, "('kyiv', ['lviv', 'sudova-vyshnia', 'zhovkva', 'busk'])\n")

    def test_invalid_input(self):
        get_unreachable_cities_for_supply('empty_input.txt', 'empty_output.txt')
        with open(
            "../resources/empty_output.txt",
            'r',
            encoding='utf-8'
        ) as file:
            first_line = file.readline()
        self.assertEqual(first_line, "-1")



if __name__ == "__main__":
    unittest.main()
