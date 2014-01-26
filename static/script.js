$("document").ready(inicializar);

var div_actualizar = "#ajax"
var ELEMENTOS = new Array();

function inicializar() {
    $("#lateral .menu li").click(
        function () {
            $("#lateral .menu li").each(
                function (index, elemento) {
                    $(elemento).attr("id", "");
                }
            );
        this.setAttribute("id", "seleccionado");
        }
    );
}

function cargar(archivo) {
    if (archivo.slice(1, 9) != "eliminar") {
        location.href = "#" + archivo;
    }
    $.ajax({
        url: archivo,
        type: "GET",
        success: respuesta_server,
        error: error_server,
    });
}

function respuesta_server(data) {
    if (data.slice(0, 5) == "error") {
        alerta(data);
    } else if (data.slice(0, 6) == "alerta") {
        alerta(data);
    } else if (data.slice(0, 13) == "redireccionar") {
        location.href = data.slice(15, data.length);
    } else {
        set_html(data);
    }
}

function error_server(data) {
    alerta("An error has ocurred");
}

function set_html(data) {
    $(div_actualizar).html(data)
}

function alerta(data) {
    data = data;
    var ventana;
    ventana = document.createElement("div");
    ventana.setAttribute("id", "mensaje");
    ventana.focus();
    
    $("#padre").append(ventana);
    
    ventana.innerHTML = data;
    
    var x, y;
    x = ventana.offsetWidth;
    y = ventana.offsetHeight;
    
    
    ventana.style.left = ((window.innerWidth / 2) - (parseInt(x) / 2) + "px");
    ventana.style.top = ((window.innerHeight / 2) - (parseFloat(y)) + "px");
    
    $("#body").click(function (){
        $("#mensaje").remove();
    });
    
}

function a() {
    var file2 = document.getElementById("archivos");

    archivos = file2.files;
    
    var divpadre = document.getElementById("filename");
    
    divpadre.innerHTML = " ";
    ELEMENTOS = []
    
    for (item=0; item < archivos.length; item++) {
        var data = archivos[item].name;
        ELEMENTOS[item] = archivos[item];
        create_div("file", divpadre, data);
    }
}

function create_div(clase, padre, data) {
    data = escape(data);
    var ventana = document.createElement("div");
    ventana.setAttribute("class", clase);
    ventana.setAttribute("title", data)
    ventana.onclick = function () {
        
        var indice = ELEMENTOS.indexOf(index);
        ELEMENTOS.splice(indice, 1);
        padre.removeChild(ventana);
    
    }
    
    padre.appendChild(ventana);
    ventana.innerHTML = data;
}

function url() {
    var direccion = document.URL;
    sdireccion = direccion.split("#/");
    if (sdireccion.length >= 2) {
        cargar("/" + sdireccion[1]);
    }
}

function subir() {
    var data = new FormData();
    
    for (file = 0; file < ELEMENTOS.length; file++) {
        data.append("file[]", ELEMENTOS[file]);
    }
    
    $.ajax({
        url: "/upload",
        type: "POST",
        contentType: false,
        data: data,
        processData: false,
        cache: false,
        success: respuesta_server
    });
}
