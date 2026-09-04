import unittest
from configlint.core import lint
class Tests(unittest.TestCase):
 def test_duplicate(self): self.assertEqual(lint('A=1\nA=2')[0].message,'duplicate key: A')
if __name__=='__main__': unittest.main()
