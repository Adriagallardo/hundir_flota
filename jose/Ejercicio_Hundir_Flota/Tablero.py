import numpy as np

class Tablero:

    def __init__(self): 
        self.tabla = self.crear_tabla()

    def crear_tabla(self):
        tabla = np.pad(np.full((10,10), fill_value="~", dtype='<U2'), pad_width=1, mode='edge')[:-1, :-1]
        tabla[0, :] = np.arange(-1, 10)
        tabla[:, 0] = np.arange(-1, 10)
        tabla[0, 0] = ' ' 
        return tabla