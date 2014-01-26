# -*- coding: utf-8 -*-

import os, time

from werkzeug import secure_filename
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import Flask
from flask import escape

import plugin_load
from core import pytohtml, general

UPLOAD_FOLDER = "tmp"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        files = request.files.getlist('file[]')
        if files:
            for f in files:
                filename = secure_filename(f.filename)
                path = app.config["UPLOAD_FOLDER"]
                f.save(os.path.join(path, filename))
            return "redireccionar: /#/files"
        else:
            return "redireccionar: /#/upload"
            
    return render_template("upload.html")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/files")
def files():
    files = os.listdir("tmp")
    dic = {}
    for sFile in files:
		
        if "." in sFile:
            extension = sFile.split(".")[-1]
            if dic.has_key(extension):
                dic[extension].append(sFile) # + ':%s' % str(time.ctime(os.stat('tmp/%s' % sFile)[9]) ))
            else:
                dic[extension] = []
                dic[extension].append(sFile) # + ':%s' % str(time.ctime(os.stat('tmp/%s' % sFile)[9]) ))

    return render_template("files.html", dic=dic, amount=len(files))

@app.route("/view/<sFile>")
def view(sFile):
    ext = False
    data = []
    #linea para corregir la apertura de sFiles en cualquier directorio
    #sFile = secure_filename(sFile)
    if os.path.isfile(os.path.join("tmp", sFile)):
        _, extension = os.path.splitext(sFile)
        extra = general.informacion("tmp/%s" % sFile.encode("ascii"))
        time_dat = str(time.ctime(os.stat('tmp/%s' % sFile)[9]) )
        for key in lista:
			if extension[1:].lower() in lista[key]["extensions"]:
				if lista[key]["active"]:
					data.append(pytohtml.pytohtml(lista[key]["functions"](os.path.join("tmp", sFile))))
				else:
					ext = True
        if data:
            return render_template("view.html", data=data, sFile=sFile, extra=extra, time_dat=time_dat)
        elif ext:
			#usando escape() para escapar las excepciones y evitar el xss
            return "error: The plugin {0} is desactivated".format(escape(extension))
        else:
            return "error: There are not extensions for the file {0}".format(escape(extension))
    else:
        return "error: It's not a file"

@app.route("/config")
def config():
    return render_template("plugins.html", plugins=lista, sFile=u"Plugins")

@app.route("/desactivate/<plugin>")
def desactivate_plugin(plugin):
    global lista
    if lista.has_key(plugin):
        lista[plugin]["active"] = False
        return redirect(url_for("config"))

@app.route("/activate/<plugin>")
def activate_plugin(plugin):
    global lista
    if lista.has_key(plugin):
        lista[plugin]["active"] = True
        return redirect(url_for("config"))

@app.route("/reload")
def reload_plugin():
    global lista
    lista = plugin_load.Core("modulos").plugins
    return redirect(url_for("config"))

@app.route("/delete/<sFile>")
def delete(sFile):
    filename = secure_filename(sFile)
    path = app.config["UPLOAD_FOLDER"]
    ruta = os.path.join(path, filename)
    if os.path.isfile(ruta):
        os.remove(ruta)
        return "redireccionar: /#/files"
    return redirect("/upload")

if __name__ == "__main__":
    lista = plugin_load.Core("modulos").plugins
    app.run(debug=True)
