import json
guardar_partida(dict_posciones, datos_enemigos):
    with open('Partidas_guardadas/partidas.json', 'a+') as partida:
        json.dump([dict_posiciones, datos_enemigo], partida, indent=4)