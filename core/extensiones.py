# -*- coding: utf-8 -*-

from mmap import mmap
from os import rename
from sys import stderr

KEYS = {
    "25504446": "pdf",
    "ffd8ffe0": "jpg",
    "d0cf11e0a1b1": "doc",
    "474946383761": "gif",
    "52494646": "wav",
    "57415645": "wav",
    "4d5a": "exe",
    "494433":"ID3",
    "89504e470d0a1a0a": "png",
    "504b0304": "zip",
    "526172211a0700": "rar",
}

def main(archivo):
    file_open = map_file(archivo)
    
    if file_open:
        return ext(file_open)
    
def map_file(archivo):
    try:
        with open(archivo, "r+b") as fd:
            mm = mmap(fd.fileno(), 0)
            bytes = mm[: n_bytes()]
            mm.close()
            return bytes.encode("hex")
    except Exception as e:
        print >> stderr, e
        return False

def n_bytes():
    return max(map(len, KEYS.keys())) / 2

def ext(bytes):
    for cabecera in KEYS.keys():
        if (cabecera in bytes) or (bytes in cabecera):
            return KEYS[cabecera]
    return False

if __name__ == "__main__":
    print main("/home/once/Desktop/taller")