from Tablero import Tablero
from Barcos import Barcos
import os, json


def preguntar(Tablero, diccionario_posiciones):
    y = int(input('Selecciona la posicion y: '))
    x = int(input('Selecciona la posicion x: '))
    prediccion = (y, x)
    encontrado = False
    for k, v in diccionario_posiciones.items():
        if prediccion in v:
            Tablero.tabla[y][x] = 'x' # Cuidado
            k.vida -= 1
            encontrado = True
            os.system('clear')
            if k.vida == 0:
                print('BARCO DESTRUIDOOOO')
            else:
                print('Barco tocado!')
            break
    if not encontrado:
        Tablero.tabla[y][x] = 'o'
        os.system('clear')
        print('Agua')
    mesa_de_juego.mostrar_pantalla()

def empiece_partida():
    lista_posiciones = []
    for barco in lista_barcos:
        while True:
            try:
                #os.system('clear')
                mesa_de_juego.mostrar_pantalla()
                input_colocacion = input(f'Introduce la posicion del {barco.nombre}: ')
                if 'h' in input_colocacion:
                    barco.establecer_orientacion('h')
                    y_input = int((input_colocacion.split('h'))[0])
                    x_input = int(((input_colocacion.split('h'))[1].split(':'))[0])
                    barco.colocar_barco(y_input, x_input, mesa_de_juego, lista_posiciones)
                    lista_posiciones.append(barco.posicion) # Añadir a la lista para chequear que dos barcos no choquen
                    break
                else:
                    barco.establecer_orientacion('v')
                    y_input = int((input_colocacion.split('v'))[0])
                    x_input = int(((input_colocacion.split('v'))[1].split(':'))[0]) #Muy lioso?, Solo me importa la primera coordenada de columna_inicio : columna_final
                    barco.colocar_barco(y_input, x_input, mesa_de_juego, lista_posiciones)
                    lista_posiciones.append(barco.posicion)
                    break
            except Exception as err:
                print(err)
        
        print(barco.posicion) # --NO

mesa_de_juego = Tablero(10, 10)
primer_barco_2_1 = Barcos('Primer barco 2x1', 2)
segundo_barco_2_1 = Barcos('Segundo barco 2x1', 2)
tercer_barco_2_1 = Barcos('Tercer barco 2x1', 2)
cuarto_barco_2_1 = Barcos('Cuarto barco 2x1', 2)
primer_barco_3_1 = Barcos('Primer barco 3x1', 3)
segundo_barco_3_1 = Barcos('Segundo barco 3x1', 3)
tercer_barco_3_1 = Barcos('Tercer barco 3x1', 3)
primer_barco_4_1 = Barcos('Primer barco 4x1', 4)
segundo_barco_4_1 = Barcos('Segundo barco 4x1', 4)
primer_barco_5_1 = Barcos('Primer barco 5x1', 5)
lista_barcos = [primer_barco_2_1, segundo_barco_2_1, tercer_barco_2_1, cuarto_barco_2_1, primer_barco_3_1, segundo_barco_3_1, tercer_barco_3_1, primer_barco_4_1, segundo_barco_4_1, primer_barco_5_1]
empiece_partida()
dict_posiciones = {barco.nombre : barco.posicion for barco in lista_barcos}
with open('posiciones.json', 'w+') as pos:
    json.dump(dict_posiciones, pos, indent=4)
#mesa_de_juego.mostrar_pantalla()
#count = 0
#while count < 5:
#    preguntar(mesa_de_juego, dict_posiciones)
#    count += 1

