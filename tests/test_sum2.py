from unittest import TestCase, main
import functools

def second_sum(numbers):
  return functools.reduce(lambda a, b: a+b, numbers)

class TestSum2(TestCase):
  def test_output(self):
    arr = [1,2,3,4,5]
    output = second_sum(arr)
    self.assertEqual(output, 15)

if __name__ == "__main__":
  main()