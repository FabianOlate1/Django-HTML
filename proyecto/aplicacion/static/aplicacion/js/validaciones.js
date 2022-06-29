//Login
var nombre = document.getElementById('nombre');
var pass = document.getElementById('pass');

var error = document.getElementById('error');


function enviarform(){
    console.log('Enviando....')

    var mensajeerror=[];

    if(nombre.value === null || nombre.value === ''){
        mensajeerror.push('Ingrese un nombre');
    }

    if(pass.value === null || pass.value === ''){
        mensajeerror.push('Ingrese una contraseña');
    }

    error.innerHTML = mensajeerror.join(', ')

    return false
};

