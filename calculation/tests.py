from django.test import TestCase
from .serializer import CalculationSerializer
from beam_calculation.settings import PWD
from json import loads

# Create your tests here.
class TestBeam(TestCase):
    def test_get_moment(self):
        self.assertEqual(CalculationSerializer().get_moment(10, 2), 20)

    def test_get_moment_None(self):
        self.assertEqual(CalculationSerializer().get_moment(None,None), None)

    def test_get_resistance_module_divisao_zero(self):
        self.assertEqual(CalculationSerializer().get_resistance_module(0,0), 0)

    def test_get_resistance_module_force_zero(self):
        self.assertEqual(CalculationSerializer().get_resistance_module(10,0),0)

    def test_get_resistance_module(self):
        self.assertEqual(CalculationSerializer().get_resistance_module(10,10),1)

    def test_get_resistance_module_table(self):
        list_json = loads(open(PWD+'\properties.json','r').read())
        list_json = sorted(list_json,key=lambda item:item['eixoxx']['mm3'])
        resistance_module = CalculationSerializer().transform_units(0.0001)
        item, last_item = CalculationSerializer().get_resistance_module_table(resistance_module,list_json)
        self.assertEqual(item,list_json[1])

    def test_fake(self):
        x = 2
        assert x == 2

if __name__ == '__main__':
    unittest.main()