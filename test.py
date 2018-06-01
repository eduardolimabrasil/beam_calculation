#Here we will do tests
import unittest
from beam_calculation import *


class TestBeam(unittest.TestCase):
    def test_get_moment(self):
        assert get_moment(10, 2) == 20

    def test_get_moment_None(self):
        assert get_moment(None,None) == None

    def test_get_resistance_module_divisao_zero(self):
        assert get_resistance_module(0,0) == 0

    def test_get_resistance_module_force_zero(self):
        assert get_resistance_module(10,0) == 0

    def test_get_resistance_module(self):
        assert get_resistance_module(10,10) == 1

    def test_get_resistance_module_table(self):
        lista = [ {
        "area":2290,
        "eixoxx":{
            "mm3":120,
            "mm4":9.19,
            "mm":63.3
        }
    }]
        assert get_resistance_module_table(10000,lista) == 120 * (10**3)
if __name__ == '__main__':
    unittest.main()



