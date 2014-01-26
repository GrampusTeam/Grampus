# -*- coding: utf-8 -*-

def pytohtml(py):
    html = []
    for tag, valor in sorted(py.iteritems()):
        tipo = type(valor).__name__
        
        if tipo == "dict":
            print "Diccionario", valor
            for dtag, dvalor in valor.iteritems():
                html.append((dtag, decode(dvalor)))
        elif tipo == "list":
            if len(valor):
                html += [(tag, decode(x)) for x in valor if x]
        else:
            if valor:
                html.append((tag, decode(valor)))

    return html


def decode(x):
    try:
        x = unicode(x.decode("unicode-escape"))
        return x
    except:
        return x

a = {
    "dict": {"a", "a"},
    "b": 0,
    1: ("1", 2),
}

pytohtml(a)