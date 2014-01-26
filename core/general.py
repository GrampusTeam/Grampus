import hashlib
import os


def informacion(archivo):
    info = {}
    sha1 = hashlib.sha1()
    f = open(archivo, "r")
    for line in f.readlines():
        sha1.update(line)
    f.close()
    
    info["sha1"] = sha1.hexdigest()
    info["size"] = str(os.path.getsize(archivo)) + " bytes"

    return info
