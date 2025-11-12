import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from app import greet

class TestApp(unittest.TestCase):
    def test_greet(self):
        # Adapt this to your name to satisfy the lab’s expectation
        self.assertEqual(greet("World"), "Hello, World!")
        # If your instructor wants the “from FirstName LastName!” suffix, change accordingly:
        # self.assertEqual(greet("World"), "Hello, World from Nour Fawaz!")
        
if __name__ == "__main__":
    unittest.main()
