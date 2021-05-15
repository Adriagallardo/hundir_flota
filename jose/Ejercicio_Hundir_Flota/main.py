from Tablero import Tablero
from Barcos import Barcos
import numpy as np
import os, json, random

def quien_empieza():
    return random.randint(1, 6), random.randint(1, 6)

def crear_json_posiciones(nombre_archivo : str):
    '''
    Esta función crea un archivo JSON con el nombres pasado por parametro que contiene las posiciones
    de los barcos escogidos.
    '''
    with open(nombre_archivo, mode='w+') as pos:
        datos_enemigo = json.dump(dict_posiciones, pos, indent=4)

def actualizar_marcadores(ganado_jose : bool):
    '''
    Esta función actualiza el JSON 'marcadores.json', que describe el historial de partidas jugadas.
    El ganador sumara +1 a su puntación 
    '''
    with open('marcador.json', 'r') as archivo:
        marcador = json.load(archivo)
    if ganado_jose:
        marcador['Jose'] += 1
    else:
        marcador['Adria'] += 1
    with open('marcador.json', 'w') as archivo:  
        json.dump(marcador, archivo, indent=4)


def ataque(Tablero, diccionario_posiciones):
    print('Defiende')
    y = int(input('Selecciona la posicion y: '))
    x = int(input('Selecciona la posicion x: '))
    os.system('clear')
    prediccion = (y + 1, x + 1)
    encontrado = False
    for Barco in lista_barcos:
        if prediccion in Barco.posicion:
            Tablero.tabla[y + 1][x + 1] = 'x'
            Barco.posicion.remove(prediccion)
            encontrado = True
            if not Barco.posicion:
                Barco.muerte = True
                print('BARCO DESTRUIDO :(')
                break
            else:
                print('Barco tocado!')
                break
    
    if not encontrado:
        Tablero.tabla[y + 1][x + 1] = 'o'
        print('Agua')

    print(np.concatenate((mesa_de_juego.tabla, separador, tablero_diana.tabla), axis=1))

    

def defensa(tablero_diana, lista_barcos_enemigos):
    print('Ataca')
    y = int(input('Selecciona la posicion y: '))
    x = int(input('Selecciona la posicion x: '))
    os.system('clear')
    prediccion = [y + 1, x + 1]
    encontrado = False
    for barco in lista_barcos_enemigos:
        if prediccion in barco.posicion:
            tablero_diana.tabla[y + 1][x + 1] = 'x' 
            barco.posicion.remove(prediccion)
            encontrado = True
            if not barco.posicion:
                barco.muerte = True
                print('BARCO DESTRUIDO :)')
                break
            else:
                print('Barco tocado')
                break

    if not encontrado:
        tablero_diana.tabla[y + 1][x + 1] = 'o'
        print('Agua')

    print(np.concatenate((mesa_de_juego.tabla, separador, tablero_diana.tabla), axis=1))
 
def empiece_partida():
    lista_posiciones = []
    for barco in lista_barcos:
        while True:
            try:
                
                
                input_colocacion = input(f'Introduce la posicion del {barco.nombre}: ')
                if 'h' in input_colocacion:
                    orientacion = 'Horizontal'
                    y_input = int((input_colocacion.split('h'))[0])
                    x_input = int(((input_colocacion.split('h'))[1].split(':'))[0])
                    barco.colocar_barco(y_input + 1, x_input + 1, mesa_de_juego, orientacion)
                    break
                else:
                    orientacion = 'Vertical'
                    y_input = int((input_colocacion.split('v'))[0])
                    x_input = int(((input_colocacion.split('v'))[1].split(':'))[0])
                    barco.colocar_barco(y_input + 1, x_input + 1, mesa_de_juego, orientacion)
                    
                    break
            except Exception as err:
                print(err)

np.set_printoptions(linewidth=100)

mesa_de_juego = Tablero()
tablero_enemigo = Tablero()
tablero_diana = Tablero()
separador = np.full((11, 1), '|')
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

#crear_json_posiciones(nombre_archivo=) # Opcional si quieres construir una archivo JSON con las posiciones elegias

with open('posiciones.json', mode='r+') as pos:
    datos_enemigo = json.load(pos)

lista_barcos_enemigos = []
for k, v in datos_enemigo.items():
    k = Barcos(k, len(v))
    for posicion in v:
        k.posicion.append(posicion)
    lista_barcos_enemigos.append(k)
# Creamos una instancia de Barco por cada elemento que hemos cargado del archivo JSON
# Ademas construimos una lista de listas de tuplas donde se guardara la posicion que ocupa cada barco


empieza_jose, empieza_adria = quien_empieza()
while empieza_jose == empieza_adria:
    empieza_jose, empieza_adria = quien_empieza()

os.system('clear')
print(np.concatenate((mesa_de_juego.tabla, separador, tablero_diana.tabla), axis=1))
ganador_jose = None
while empieza_jose > empieza_adria:
    lista_vida_barcos = [barco.muerte for barco in lista_barcos]
    lista_vida_barcos_enemigos = [barco.muerte for barco in lista_barcos_enemigos]
    if all(lista_vida_barcos) or all(lista_vida_barcos_enemigos):
        if all(lista_vida_barcos):
            print('Has perdido')
            ganador_jose = False
            break
        else:
            print('Has ganado')
            ganador_jose = True
        break
    ataque(mesa_de_juego, lista_barcos)
    defensa(tablero_diana, lista_barcos_enemigos)

while empieza_jose < empieza_adria:
    lista_vida_barcos = [barco.muerte for barco in lista_barcos]
    lista_vida_barcos_enemigos = [barco.muerte for barco in lista_barcos_enemigos]
    if all(lista_vida_barcos) or all(lista_vida_barcos_enemigos):
        if all(lista_vida_barcos):
            print('Has perdido')
            ganador_jose = False
        else:
            print('Has ganado')
            ganador_jose = True
        break
    defensa(tablero_diana, lista_barcos_enemigos)
    ataque(mesa_de_juego, lista_barcos)

actualizar_marcadores(ganador_jose)   
print('Partida terminada')
