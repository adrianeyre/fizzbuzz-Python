import unittest
import fizzbuzz

class TestFizzbuzz(unittest.TestCase):

    def test_fizzbuzz_one(self):
        self.assertEqual(fizzbuzz.fizzbuzz(1), 1)

    def test_fizzbuzz_three(self):
        self.assertEqual(fizzbuzz.fizzbuzz(3), 'fizz')

    def test_fizzbuzz_five(self):
        self.assertEqual(fizzbuzz.fizzbuzz(5), 'buzz')

    def test_fizzbuzz_fifteen(self):
        self.assertEqual(fizzbuzz.fizzbuzz(15), 'fizzbuzz')

if __name__ == '__main__':
    unittest.main()
