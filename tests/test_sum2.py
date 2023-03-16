from unittest import TestCase, main
from fractions import Fraction
import functools

def second_sum(numbers):
  return functools.reduce(lambda a, b: a+b, numbers)

class TestSum2(TestCase):
  def test_output(self):
    arr = [1,2,3,4,5]
    output = second_sum(arr)
    self.assertEqual(output, 15)
  
  def test_bad_scenario(self):
    arr = [Fraction(1, 2), Fraction(1, 2)]
    output = second_sum(arr)

    with self.assertRaises(AssertionError):
      self.assertIsInstance(output, int)


if __name__ == "__main__":
  main()