import unittest
import sys
sys.path.insert(0, "../typing")

from palindrome import palindrome

class PalindromeTestCase(unittest.TestCase):
    def test_palindrome(self):
        non_pal = palindrome("Irving")
        self.assertEqual(non_pal, False)

        self.assertEqual(palindrome("ana"), True)
        self.assertEqual(palindrome("Ligar es ser agil"), True)

if __name__ == "__main__":
    unittest.main()