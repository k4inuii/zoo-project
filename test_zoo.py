import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    def test_teen_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(15), 100)

    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(30), 150)
       
       
    def test_old_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(81), 100)

    def test_pregnant_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "Invalid Age")

    def test_child_ticket_price1(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
       
    def test_child_ticket_price2(self):
        self.assertEqual(self.zoo.get_ticket_price(1), 50)

    def test_child_ticket_price3(self):
        self.assertEqual(self.zoo.get_ticket_price(11), 50)

    def test_child_ticket_price4(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

    def test_teen_ticket_price1(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)

    def test_teen_ticket_price2(self):
        self.assertEqual(self.zoo.get_ticket_price(14), 100)

    def test_teen_ticket_price3(self):
        self.assertEqual(self.zoo.get_ticket_price(19), 100)

    def test_teen_ticket_price4(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_adult_ticket_price1(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)

    def test_adult_ticket_price2(self):
        self.assertEqual(self.zoo.get_ticket_price(22), 150)

    def test_adult_ticket_price3(self):
        self.assertEqual(self.zoo.get_ticket_price(59), 150)

    def test_adult_ticket_price4(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

    def test_old_ticket_price1(self):
        self.assertEqual(self.zoo.get_ticket_price(69), 100)
if __name__ == '__main__':
    unittest.main()