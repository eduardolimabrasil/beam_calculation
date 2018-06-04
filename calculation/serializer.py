from .models import Calculation
from rest_framework import serializers
from .models import Calculation
from json import loads
from beam_calculation.settings import PWD

class CalculationSerializer(serializers.ModelSerializer):
    class Meta():
        model = Calculation
        fields = '__all__'

    def resistance_module(self, input_json):
        moment = self.get_moment(input_json.get('force'), input_json.get('distance'))
        resistance_module = self.get_resistance_module(input_json.get('allowable_stress'),moment)
        resistance_module = self.transform_units(resistance_module)
        list_json = loads(open(PWD+'\properties.json','r').read())
        list_json = sorted(list_json,key=lambda item:item['eixoxx']['mm3'])
        return self.get_resistance_module_table(resistance_module, list_json)

    def get_moment(self, force , distance):
        if force and distance:
            return force * distance
        else:
            return None

    def get_resistance_module(self, allowable_stress, moment):
        """allowable_stress not to be a 0
        """
        if allowable_stress and moment and allowable_stress>0:
            return moment / allowable_stress
        else:
            return 0

    def transform_units(self, allowable_stress):
        '''return:
        high most next table value to resistance module '''
        return allowable_stress * (10**9)

    def get_resistance_module_table(self, resistance_module, list_output):
        choice_item = {"eixoxx":{"mm3":0}}
        last_item = choice_item
        for item in list_output:
            result = item['eixoxx']['mm3'] * (10**3)
            if result > resistance_module:
                break
            last_item = item
        return item, last_item