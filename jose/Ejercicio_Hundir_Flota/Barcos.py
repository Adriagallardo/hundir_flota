class Barcos:

    def __init__(self, nombre, largo):
        
        self.nombre = nombre
        self.largo = largo
        self.orientacion = None
        self.posicion = []
        self.muerte = False


    def colocar_barco(self, coordenada_y, coordenada_x, Tabler, orientacion):
        diccionario_orientaciones = {'Norte' :0, 'Sur' :1, 'Este': 2, 'Oeste':3}
        while True:

            x_inicial = coordenada_x
            y_inicial = coordenada_y
            orientacion = orientacion

            #if diccionario_orientaciones[orientacion] == 0: # Norte
                #if (y_inicial - 4 < 1) or not all(Tabler.tabla[y_inicial -3 : y_inicial + 1, x_inicial] == '~'):
                # La primer condicion es verdad si el indice se va fuera del rango de la matriz
                # La segunda es verdad si hay algun barco o casilla ya marcada en el rango donde ira el barco
                # Si alguna es verdad el bucle se reiniciara y se utilizaran otras coordenadas
                    #continue
                #for i in range(y_inicial, y_inicial - 4, -1):
                    #Tabler.tabla[i][x_inicial] = '#'

            if diccionario_orientaciones[orientacion] == 1: # Sur
                if (y_inicial + self.largo > 11) or not all(Tabler.tabla[y_inicial : y_inicial + self.largo, x_inicial] == '~'):
                    raise Exception('No podemos crearlo ahí en vertical.')
                for i in range(y_inicial, y_inicial + self.largo):
                    self.posicion.append((i, x_inicial))
                    Tabler.tabla[i][x_inicial] = '#'

            elif diccionario_orientaciones[orientacion] == 2: # Este
                if (x_inicial + self.largo > 11) or not all(Tabler.tabla[y_inicial, x_inicial: x_inicial + self.largo] == '~'):
                    raise Exception('No podemos crearlo ahí en horizontal.')
                for i in range(x_inicial, x_inicial + self.largo):
                    self.posicion.append((y_inicial, i))
                    Tabler.tabla[y_inicial][i] = '#'
                    
            #elif diccionario_orientaciones[orientacion] == 3: # Oeste
                #if (x_inicial - 4 < 1) or not all(Tabler.tabla[y_inicial, x_inicial -3 :x_inicial + 1] == '~'):
                    #continue
                #for i in range(x_inicial, x_inicial - 4, -1):
                    #Tabler.tabla[y_inicial][i] = '#'
                    
            break

        print(f'Añadido barco de eslora 4 en la posicion inicial {(y_inicial-1, x_inicial-1)} con orientacion {orientacion}')
        print(Tabler.tabla)     
    
    def establecer_orientacion(self, orientacion):
        self.orientacion = orientacion