
#tensao_admicivel = momento * (distancia/ momento_inercia)

#tensao_admicivel = 10



def calculo_momento(forca , distancia):
    return forca * distancia

def get_modulo_resistencia(tensao_admicivel, momento):
    #maior mais próximo da tabela ao valor 
    modulo_resistencia = momento / tensao_admicivel
    return modulo_resistencia

if __name__ == '__main__':
    forca = 2 * (10**6)
    distancia = 2
    momento = calculo_momento(forca, distancia)
    print("momento:{0}".format(str(momento)))
    modulo_resistencia = get_modulo_resistencia(12, momento)
    print("modulo resistencia:{0}".format(str(modulo_resistencia)))


