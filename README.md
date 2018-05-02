# FizzBuzz-Python
#### Technologies: Python, unittest

* [Setting up the application](#setup)
* [Unit Tests](#tests)
* [Python](#code)

## The Challenge ##
The challenge was to make a simple “FizzBuzz” program that accepted one integer value into a function called fizzBuzz. The function checks for the following conditions: if the integer is divisible by 3 it returns ‘Fizz’, if the integer is divisible by 5 it returns ‘Buzz’, if the integer is divisible by 3 and 5 it returns ‘FizzBuzz’ and if none of the conditions are met it returns the integer. Example below
```shell
1 --> 1
2 --> 2
3 --> Fizz
4 --> 4
5 --> Buzz
6 --> Fizz
7 --> 7
8 --> 8
9 --> Fizz
10 --> Buzz
11 --> 11
12 --> Fizz
13 --> 13
14 --> 14
15 --> FizzBuzz
16 --> 16
17 --> 17
18 --> Fizz
19 --> 19
20 --> Buzz
```

## <a name="setup">Setting up the applicaion</a>
```
$ git clone https://github.com/adrianeyre/fizzbuzz-Python
$ cd fizzbuzz-Python
```

## <a name="tests">Unit Tests</a> ##

```python
def fizzbuzz(num):
    result = ""
    if num % 3 == 0: result += "fizz"
    if num % 5 == 0: result += "buzz"
    return num if result == "" else result

```

## <a name="code">Python Code</a> ##
```python
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
```
