# -*- coding: utf-8 -*-

import os
import re

class Core(object):
    
    def __init__(self, route):
        self.plugins = {}
        self.load_plugins(route)
    
    def load_plugins(self, route):
        """Carga los plugins y su configuración"""
        for sFile in os.listdir(route):
            plugin_route = os.path.join(route, sFile)
            
            if os.path.isfile(plugin_route):
                if re.match("[a-z].*\.py$", sFile, re.I):
                    try:
                        mod = __import__("{0}.{1}".format(route, sFile[:-3]))
                        mod = getattr(mod, sFile[:-3])
                    except ImportError as e:
                        print e.args[0]

                    if hasattr(mod, "grampus_modulo"):
                        print "Loading:", plugin_route
                        tipo, funcion, param = mod.grampus_modulo()
                        self.plugins[sFile] = {}
                        self.plugins[sFile]["extensions"] = param
                        self.plugins[sFile]["functions"] = funcion
                        self.plugins[sFile]["active"] = True
                        self.plugins[sFile]["name"] = sFile
