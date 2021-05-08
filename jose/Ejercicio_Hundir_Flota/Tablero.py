import numpy as np

class Tablero:

    def __init__(self): ##Integrar funcion pad
        #self.altura = altura
        #self.anchura = anchura
        self.tabla = crear_tabla()#np.full((10,10), fill_value="~")

    #def mostrar_pantalla(self):
        #for i in range(self.altura + 1):
            #print(' '.join(self.tabla[i]))

def crear_tabla():
    tabla = np.pad(np.full((10,10), fill_value="~", dtype='<U2'), pad_width=1, mode='edge')[:-1, :-1]
    tabla[0, :] = np.arange(-1, 10)
    tabla[:, 0] = np.arange(-1, 10)
    tabla[0, 0] = ' ' 
    return tabla
    

tabla = Tablero()
print(tabla.tabla.dtype)
#tabla.crear_tabla()
#print(tabla.tabla)
# np.pad(np.full((10,10), fill_value="~"), pad_width=1, mode='edge')[:-1, :-1]
