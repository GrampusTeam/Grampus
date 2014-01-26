import os
import tempfile
import shutil


def listar(directorio):
    """Regresa uns lista con los archivos contenidos
    en unca carpeta"""
    archivos = os.listdir(directorio)
    buff = []
    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        if os.path.isfile(ruta):
            buff.append(ruta)
    return buff
    


def crear(prefijo="Gram"):
    """Crea una carpeta temporal y regresa un string con la ruta
    la variable prefijo define el prefijo que se usara para la
    carpeta, por defecto se usara Gram"""
    temp = tempfile.mkdtemp(prefix=prefijo)
    return temp

def eliminar(ruta):
    """Elimina un directorio, toma como parametro la ruta del directorio
    a eliminar"""
    shutil.rmtree(ruta)