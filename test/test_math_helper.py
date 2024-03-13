import sys
from unittest import TestCase

import math_helper as mh

class Test(TestCase):
    def test_value(self):
        pass

    def test_bisection(self):
        #self.assertEqual(mh.bisection(0, 4, '3', 1000), (1.5707963267948966, 50))
        value = mh.bisection(0, 4, '3', 50)
        print()
        print("Value: " + str(value[0]) + " Iterations: " + str(value[1]))


    def test_second_method(self):
        value = mh.second_method(0, 4, '4', 15)
        print()
        print("Value: " + str(value[0]) + " Iterations: " + str(value[1]))
        mh.draw_plot('4', value)

