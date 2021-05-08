from Tablero import Tablero
from Barcos import Barcos
import os, json, random

def quien_empieza():
    return random.randint(1, 6), random.randint(1, 6)


def ataque(Tablero, diccionario_posiciones):
    print('Defiende')
    y = int(input('Selecciona la posicion y: '))
    x = int(input('Selecciona la posicion x: '))
    prediccion = (y, x)
    encontrado = False
    for Barco in lista_barcos:
        if prediccion in Barco.posicion:
            Tablero.tabla[y][x] = 'x' # Cuidado
            Barco.posicion.remove(prediccion)
            encontrado = True
            #os.system('clear')
            if not Barco.posicion:
                Barco.muerte = True
                print('BARCO DESTRUIDOOOO')
                break
            else:
                print('Barco tocado!')
                break
    
    if not encontrado:
        Tablero.tabla[y][x] = 'o'
        #os.system('clear')
        print('Agua')

    print(Tablero.tabla)

    

def defensa(tablero_diana, lista_barcos_enemigos):
    print('Ataca')
    y = int(input('Selecciona la posicion y: '))
    x = int(input('Selecciona la posicion x: '))
    prediccion = [y, x]
    encontrado = False
    for barco in lista_barcos_enemigos:
        if prediccion in barco.posicion:
            tablero_diana.tabla[y][x] = 'x' # Cuidado
            barco.posicion.remove(prediccion)
            encontrado = True
            #os.system('clear')
            if not barco.posicion:
                barco.muerte = True
                print('BARCO DESTRUIDO :)')
                break
            else:
                print('Barco tocado')
                break

    if not encontrado:
        tablero_diana.tabla[y][x] = 'o'
        #os.system('clear')
        print('Agua')

    print(tablero_diana.tabla)
    
def empiece_partida():
    lista_posiciones = []
    for barco in lista_barcos:
        while True:
            try:
                #os.system('clear')
                
                input_colocacion = input(f'Introduce la posicion del {barco.nombre}: ')
                if 'h' in input_colocacion:
                    orientacion = 'Este'
                    #barco.establecer_orientacion('h')
                    y_input = int((input_colocacion.split('h'))[0])
                    x_input = int(((input_colocacion.split('h'))[1].split(':'))[0])
                    barco.colocar_barco(y_input + 1, x_input + 1, mesa_de_juego, orientacion)
                    # Añadir a la lista para chequear que dos barcos no choquen
                    break
                else:
                    orientacion = 'Sur'
                    #barco.establecer_orientacion('v')
                    y_input = int((input_colocacion.split('v'))[0])
                    x_input = int(((input_colocacion.split('v'))[1].split(':'))[0]) #Muy lioso?, Solo me importa la primera coordenada de columna_inicio : columna_final
                    barco.colocar_barco(y_input + 1, x_input + 1, mesa_de_juego, orientacion)
                    
                    break
            except Exception as err:
                print(err)

            print(mesa_de_juego.tabla) # --NO

mesa_de_juego = Tablero()
tablero_enemigo = Tablero()
tablero_diana = Tablero()
#print(mesa_de_juego.tabla, tablero_enemigo.tabla, sep='\t') Ver las dos matrices a la vez

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
mesa_de_juego.tabla
empiece_partida()
dict_posiciones = {barco.nombre : barco.posicion for barco in lista_barcos}
#with open('posiciones.json', mode='w+') as pos:
#    datos_enemigo = json.dump(dict_posiciones, pos, indent=4)

with open('posiciones.json', mode='r+') as pos:
    datos_enemigo = json.load(pos)

print(tablero_enemigo.tabla)

lista_barcos_enemigos = []
for k, v in datos_enemigo.items():
    k = Barcos(k, len(v))
    for posicion in v:
        k.posicion.append(posicion)
    lista_barcos_enemigos.append(k)

print(tablero_enemigo.tabla)
empieza_jose, empieza_adria = quien_empieza()
while empieza_jose == empieza_adria:
    empieza_jose, empieza_adria = quien_empieza()

while empieza_jose > empieza_adria:
    lista_vida_barcos = [barco.muerte for barco in lista_barcos]
    lista_vida_barcos_enemigos = [barco.muerte for barco in lista_barcos_enemigos]
    if all(lista_vida_barcos) or all(lista_vida_barcos_enemigos):
        if all(lista_vida_barcos):
            print('Has perdido')
            b
        else:
            print('Has ganado')
        break
    ataque(mesa_de_juego, lista_barcos)
    defensa(tablero_diana, lista_barcos_enemigos)

while empieza_jose < empieza_adria:
    lista_vida_barcos = [barco.muerte for barco in lista_barcos]
    lista_vida_barcos_enemigos = [barco.muerte for barco in lista_barcos_enemigos]
    if all(lista_vida_barcos) or all(lista_vida_barcos_enemigos):
        if all(lista_vida_barcos):
            print('Has perdido')
        else:
            print('Has ganado')
        break
    defensa(tablero_diana, lista_barcos_enemigos)
    ataque(mesa_de_juego, lista_barcos)
    
print('Partida terminada')
