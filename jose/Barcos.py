class Barcos:

    def __init__(self, nombre, largo):
        
        self.nombre = nombre
        self.largo = largo
        self.orientacion = None
        self.posicion = []
        self.vida = largo


    def colocar_barco(self, coordenada_y, coordenada_x, Tablero, lista_posiciones):
        if coordenada_y == 0 or coordenada_y > 10 or coordenada_x == 0 or coordenada_x > 10:
            raise Exception('Fuera de rango')

        if self.orientacion == 'h':
            if coordenada_x + self.largo > 10:
                raise Exception('Fuera de rango')
            for i in range(coordenada_y, coordenada_y + self.largo): # Para ver si choco co un barco
                for j in range(len(lista_posiciones)):
                    if (coordenada_y, i) in lista_posiciones[j]:
                        raise Exception('Has chocado con un barco')
            for i in range(coordenada_x, coordenada_x + self.largo):                      
                self.posicion.append((coordenada_y, i))
                Tablero.tabla[coordenada_y][i] = '#'
        
        if self.orientacion == 'v':
            if coordenada_y + self.largo > 10:
                raise Exception('Fuera de rango')
            for i in range(coordenada_y, coordenada_y + self.largo): # Para ver si choco co un barco
                for j in range(len(lista_posiciones)):
                    if (i, coordenada_x) in lista_posiciones[j]:
                        raise Exception('Has chocado con un barco')
            for i in range(coordenada_y, coordenada_y + self.largo):
                self.posicion.append((i, coordenada_x))
                Tablero.tabla[i][coordenada_x] = '#'         
    
    def establecer_orientacion(self, orientacion):
        self.orientacion = orientacion