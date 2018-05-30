
#allowable_stress = moment * (distance/ moment_inercia)

#allowable_stress = 10



def get_moment(force , distance):
    return force * distance

def get_resistance_module(allowable_stress, moment):
    #high most next table value 
    resistance_module = moment / allowable_stress
    return resistance_module

if __name__ == '__main__':
    force = input("Please get a force:")
    distance = input("Please get a distance:")
    moment = get_moment(float(force), float(distance))
    print("moment:{0}".format(str(moment)))
    resistance_module = get_resistance_module(12, moment)
    print("modulo resistencia:{0}".format(str(resistance_module)))


