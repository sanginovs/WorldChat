import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest

from user.tests import UserTest
#every time you write a new test, add it to this file


if __name__== '__main__':
    unittest.main()