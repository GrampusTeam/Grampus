import urllib2
import urllib
import os

from core import directorio


def descargar(items, direct=None):
    agent = "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1"

    if not direct:
        #Creamos un directorio temporal
        direct = directorio.crear()
    for url in items:
        #url = urllib.quote(url)
        #print "Descargando:", url
        try:
            (server, nombre) = os.path.split(url)
            opener = urllib2.Request(url)
            opener.add_header("User-Agent", agent)
            opener.add_header("Host", opener.get_host())
            opener.add_header("Referer", opener.get_host())
            ruta = os.path.join(direct, nombre)
            data = urllib2.urlopen(opener)
            descargado = open(ruta, "wb")

            for byte in data:
                descargado.write(byte)
            descargado.close()
        except NameError:
            #print "Error descargando:", url
            pass

    return(direct)
