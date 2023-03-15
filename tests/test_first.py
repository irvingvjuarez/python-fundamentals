from unittest import TestCase

def getExactWord():
  return "Specific word"

class TestGetExactWord(TestCase):
  def test_response(self):
    res = getExactWord()
    self.assertEqual(res, "Specific word")