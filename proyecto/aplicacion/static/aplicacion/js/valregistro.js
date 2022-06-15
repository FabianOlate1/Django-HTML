var nom = document.getElementById('nom');
var ape = document.getElementById('ape');
var email = document.getElementById('email');
var psw = document.getElementById('psw');
var error = document.getElementById('error');

function enviarformu(){
    console.log('Enviando....')

    var mensajeError=[];

    if(nom.value === null || nom.value === ''){
        mensajeError.push('Ingrese un nombre');
    }

    if(ape.value === null || ape.value === ''){
        mensajeError.push('Ingrese su apellido');
    }

    if(email.value === null || email.value === ''){
        mensajeError.push('Ingrese un correo valido');
    }

    if(psw.value === null || psw.value === ''){
        mensajeError.push('Ingrese una contraseña');
    }

    error.innerHTML = mensajeError.join(', ')

    return false
};