class Barcos:

    def __init__(self, nombre, largo):
        
        self.nombre = nombre
        self.largo = largo
        self.posicion = []
        self.muerte = False


    def colocar_barco(self, coordenada_y, coordenada_x, Tabler, orientacion):
        while True:

            x_inicial = coordenada_x
            y_inicial = coordenada_y
            orientacion = orientacion

            if orientacion == 'Vertical': # Vertical
                # La primer condicion es verdad si el indice se va fuera del rango de la matriz
                # La segunda es verdad si hay algun barco o casilla ya marcada en el rango donde ira el barco
                # Si alguna es verdad se lanzara una excepción
                if (y_inicial + self.largo > 11) or not all(Tabler.tabla[y_inicial: y_inicial + 4, x_inicial] == '~'):
                    raise Exception('Noooo')
                for i in range(y_inicial, y_inicial + self.largo):
                    self.posicion.append((i, x_inicial))
                    Tabler.tabla[i][x_inicial] = '#'

            elif orientacion == 'Horizontal': # Horizontal
                if (x_inicial + self.largo > 11) or not all(Tabler.tabla[y_inicial, x_inicial: x_inicial + self.largo] == '~'):
                    raise Exception('Noooo')
                for i in range(x_inicial, x_inicial + self.largo):
                    self.posicion.append((y_inicial, i))
                    Tabler.tabla[y_inicial][i] = '#'
                    
            break

        print(f'Añadido barco de eslora 4 en la posicion inicial {(y_inicial, x_inicial)} con orientacion {orientacion}')
        print(Tabler.tabla)