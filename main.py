from Tablero import Tablero
from Barcos import Barcos
import numpy as np
import os, json, random
import pyfiglet 

def bienvenida():
    mensaje = pyfiglet.figlet_format("Bienvenido a la Batalla naval!", font="slant")
    print(mensaje)
    print('Pulsa Enter para comenzar')
    input()
    print('¡Bienvenido jugador!:\nEn este juego tendras que colocar tus 10 barcos, sin salirte del rango de navegación y sin solaparse, con el siguiente formato:\nCasilla inicial en el eje y, orientacion (h o v) y casilla inicial en el eje x.\nEjemplo 6h5: Inicio en la casilla (5,6) con orientacion horizontal.\n')
    print('Despues de crear tu tablero deberas colocar los barcos enemigos importando un archivo json como te indicaremos mas adelante.\nLa comunicación con tu oponente es muy importante.\nTanto para elegir quien comieza el ataque como para elegir las posiciones que ataca tu oponente\n¿Lo has entendido? ¿Si o No?')
    preparado = input()
    if preparado.lower() == 'no':
        print('¿No estas preparado?. Vuelve cuando lo estes.')
        exit()
    print('Empezaremos rellenando tu tablero: ')
    
def guardar_partida(dict_posciones, datos_enemigos, mi_tabla, tabla_enemiga):
    with open('Partidas_guardadas/posicion_mis_barcos.json', 'w+') as mis_barcos:
        json.dump(dict_posciones, mis_barcos, indent=4)
    with open('Partidas_guardadas/posicion_barcos_enemigos.json', 'w+') as barcos_enemigos:
        json.dump(datos_enemigos, barcos_enemigos, indent=4)
    with open('Partidas_guardadas/mi_tablero.json', 'w+') as mi_tablero:
        json.dump(mi_tabla.tabla.tolist(), mi_tablero, indent=4)
    with open('Partidas_guardadas/tablero_enemigo.json', 'w+') as tablero_enemigo:
        json.dump(tabla_enemiga.tabla.tolist(), tablero_enemigo, indent=4)

def quien_empieza():
    print('--------------')
    print('Para ver quien empieza, lanzareis cada uno un dado de 6 caras.\nDeberás introducir el valor del dado del oponente cuando te lo pidamos, no hagas trampa!')
    mi_dado = random.randint(1, 6)
    print(f'Has sacado un {mi_dado}, comunicalo a tu rival')
    dado_rival = int(input('Introduce el dado rival: '))
    if mi_dado > dado_rival:
        print(f"He sacado un {mi_dado} y el oponente un {dado_rival}. Disparo primero! ")
        return mi_dado, dado_rival
    elif mi_dado < dado_rival:
        print(f"El oponente ha sacado un {dado_rival} y yo un {mi_dado}. El oponente dispara primero! ")
        return mi_dado, dado_rival
    while mi_dado == dado_rival:
        print('--------------')
        print('Habeis sacado lo mismo. Volved a tirar')
        return quien_empieza()
    
def crear_json_posiciones(dict_posiciones : dict):
    '''
    Esta función crea un archivo JSON con los nombres pasado por parametro que contiene las posiciones
    de los barcos escogidos.
    '''
    with open('./json_usuario/archivo_rival.json', mode='w+') as rival:
        datos_enemigo = json.dump(dict_posiciones, rival, indent=4)
    print('--------------')

def actualizar_marcadores(ganado_yo : bool):
    '''
    Esta función actualiza el JSON 'marcadores.json', que describe el historial de partidas jugadas.
    El ganador sumara +1 a su puntación 
    '''
    with open('marcador.json', 'r') as archivo:
        marcador = json.load(archivo)
    if ganado_yo:
        marcador['Yo'] += 1
    else:
        marcador['Oponente'] += 1
    with open('marcador.json', 'w') as archivo:  
        json.dump(marcador, archivo, indent=4)

def defender(Tablero, diccionario_posiciones):
    print('Turno de defender. Selecciona la casilla que indique tu oponente')
    print('--------------')
    while True:
        try:
            y = int(input('Selecciona la posicion y: '))
            x = int(input('Selecciona la posicion x: '))
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
                        print('BARCO TOCADO')
                        break
            
            if not encontrado:
                Tablero.tabla[y + 1][x + 1] = 'o'
                print('AGUA')
            break
        except Exception:
            print('Estas coordenadas no son válidas')
            continue

    print(np.concatenate((mesa_de_juego.tabla, separador, tablero_diana.tabla), axis=1))
    print('--------------')

def atacar(tablero_diana, lista_barcos_enemigos):
    print('Turno de atacar. Selecciona casilla rival')
    print('--------------')
    while True:
        try:
            y = int(input('Selecciona la posicion y: '))
            x = int(input('Selecciona la posicion x: '))
            prediccion = [y + 1, x + 1]
            encontrado = False
            salir = None
            for barco in lista_barcos_enemigos:
                if prediccion in barco.posicion:
                    tablero_diana.tabla[y + 1][x + 1] = 'x' 
                    barco.posicion.remove(prediccion)
                    encontrado = True
                    if not barco.posicion:
                        barco.muerte = True
                        print('BARCO DESTRUIDO :)')
                    else:
                        print('BARCO TOCADO')
                        
            if not encontrado:
                tablero_diana.tabla[y + 1][x + 1] = 'o'
                print('AGUA')

            break
        except Exception:
            print('Estas coordenadas no son válidas')
            continue

    print(np.concatenate((mesa_de_juego.tabla, separador, tablero_diana.tabla), axis=1))
    print('--------------')
 
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
                print('Lee de nuevo las instrucciones!')

np.set_printoptions(linewidth=100)
os.system('clear')
bienvenida()
mesa_de_juego = Tablero()
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
crear_json_posiciones(dict_posiciones)

while True:
    try :
        x = input('Importa el json del rival a la carpeta con el nombre "json_rival"\nY pasale el archivo json creado en la carpeta "json_usuario"\nPulsa Enter para continuar')
        with open('json_rival/archivo_rival.json', 'r+') as rival:
            datos_enemigos = json.load(rival)
            break
    except Exception:
        print('No has importado bien.')
        pass

lista_barcos_enemigos = []
for k, v in datos_enemigos.items():
    k = Barcos(k, len(v))
    for posicion in v:
        k.posicion.append(posicion)
    lista_barcos_enemigos.append(k)
# Creamos una instancia de Barco por cada elemento que hemos cargado del archivo JSON
# Ademas construimos una lista de listas de tuplas donde se guardara la posicion que ocupa cada barco

empieza_yo, empieza_oponente = quien_empieza()
os.system('clear')
print(np.concatenate((mesa_de_juego.tabla, separador, tablero_diana.tabla), axis=1))
ganador_jose = None
print('Comienza la partida!')
while empieza_yo > empieza_oponente:
    lista_vida_barcos = [barco.muerte for barco in lista_barcos]
    lista_vida_barcos_enemigos = [barco.muerte for barco in lista_barcos_enemigos]
    if all(lista_vida_barcos) or all(lista_vida_barcos_enemigos):
        if all(lista_vida_barcos):
            print('Has perdido')
            ganador_yo = False
            break
        else:
            print('Has ganado')
            ganador_yo = True
        break
    atacar(tablero_diana, lista_barcos_enemigos)
    defender(mesa_de_juego, lista_barcos)
    guardar_partida(dict_posiciones, datos_enemigos, mesa_de_juego, tablero_diana)
    
while empieza_yo < empieza_oponente:
    lista_vida_barcos = [barco.muerte for barco in lista_barcos]
    lista_vida_barcos_enemigos = [barco.muerte for barco in lista_barcos_enemigos]
    if all(lista_vida_barcos) or all(lista_vida_barcos_enemigos):
        if all(lista_vida_barcos):
            print('Has perdido')
            ganador_yo = False
        else:
            print('Has ganado')
            ganador_yo = True
        break
    defender(mesa_de_juego, lista_barcos)
    atacar(tablero_diana, lista_barcos_enemigos)
    guardar_partida(dict_posiciones, datos_enemigos, mesa_de_juego, tablero_diana)
    
actualizar_marcadores(ganador_yo)   
print('Partida terminada')