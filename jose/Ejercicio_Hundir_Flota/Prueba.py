import json

ganado_jose = False
with open('marcador.json', 'r') as archivo:
    marcador = json.load(archivo)
if ganado_jose:
    marcador['Jose'] += 1
else:
    marcador['Adria'] += 1
with open('marcador.json', 'w') as archivo:  
    json.dump(marcador, archivo, indent=4)
