import json
ruta = "posiciones.json"
data_content = json.load(ruta.read())
print(data_content)