
#allowable_stress = moment * (distance/ moment_inercia)

#allowable_stress = 10
import json


def get_moment(force , distance):
    if force and distance:
        return force * distance
    else:
        return None

def get_resistance_module(allowable_stress, moment):
    """allowable_stress not to be a 0
    """
    if allowable_stress and moment and allowable_stress>0:
         return moment / allowable_stress
    else:
        return 0

def transform_units(allowable_stress):
    '''return:
    high most next table value to resistance module '''
    return allowable_stress * (10**9)

def get_resistance_module_table(resistance_module, list_output):
    choice_item = {"eixoxx":{"mm3":0}}
    for item in list_output:
        result = item['eixoxx']['mm3'] * (10**3)
        if result > resistance_module:
            break
    return result

if __name__ == '__main__':
    force = input("Please get a force:")
    unit_force = input("Please get a unit:")
    distance = input("Please get a distance:")
    unit_distance = input("Please get a unit:")
    allowable_stress = input("Please get allowable stress:")
    moment = get_moment(float(force), float(distance))
    print("moment:{0}".format(str(moment)))
    resistance_module = get_resistance_module(float(allowable_stress), moment)
    print("modulo resistencia:{0}".format(str(resistance_module)))
    list_output = json.loads(open('properties.json','r').read())
    list_output = sorted(list_output, key=lambda item:item['eixoxx']['mm3'])
    resistence_module_table = get_resistance_module_table(transform_units(resistance_module),list_output)
    print(resistence_module_table)




