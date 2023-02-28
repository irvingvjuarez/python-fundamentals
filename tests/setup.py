import unittest

class WidgetTestCase(unittest.TestCase):

    def setUp(self):
        self.widget = Widget("The Widget")

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50), "Incorrect default size")

    def test_widget_resize(self):
        self.widget.resize(100, 150)
        self.assertEqual(self.widget.size(), (100, 150), "Wrong size after resize")
    
    def tearDown(self):
        self.widget.dispose()

if __name__ == "__main__":
    unittest.main()