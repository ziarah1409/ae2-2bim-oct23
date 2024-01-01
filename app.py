"""
    Ejemplo del manejo de hilos
"""

import requests
import time
import csv
import threading
# librería de python que permite ejecutar comandos
import subprocess

def obtener_data():
    lista = []
    with open("informacion/data.csv") as archivo:
        lineas = csv.reader(archivo, quotechar="|")
        for row in lineas:
            # pass
            lista.append(lista.append(row[0].split("|")[1]))
    # se retorna la lista con la información que se necesita
    return lista

def worker(url):
    print("Iniciando %s %s" % (threading.current_thread().getName(), url))
    # Obtener el contenido de la URL
    response = requests.get(url)
    if response.status_code == 200:
        # Escribir el contenido en un archivo de texto
        url2=url.replace('https://', '').replace('www.', '').replace('es.wikipedia.org/wiki/', '')
        print(url2)
        with open(f"salida/"+url2+".txt", "w", encoding='utf-8') as file:
            file.write(response.text)
        print(f"Contenido de {url} guardado en archivo")
    else:
        print(f"No se pudo obtener el contenido de {url}")

    print("Finalizando %s" % (threading.current_thread().getName()))

for c in obtener_data():
    # Se crea los hilos
    # en la función
    numero = c[0]
    url = c[1]
    hilo1 = threading.Thread(name='navegando...',
                            target=worker,
                            args=(c,))
    hilo1.start()
