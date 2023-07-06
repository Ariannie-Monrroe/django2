const formulario = document.getElementById("formValidation");



formulario.addEventListener('submit',function(evento){
    evento.preventDefault();

    var pass2 = document.getElementById("passwordNuevaValidarId").value.length
    var pass1 = document.getElementById("passwordNuevoId").value.length

    if (document.getElementById("emailNuevoId").value.length == 0) {
        alert("Ingrese el correo.");
        return;
        
    }else if (document.getElementById("usernameNuevoId").value.length == 0){
        alert("Ingrese el Nombre.");
        return;
        
    }else if(pass1 == 0){
        alert("Ingrese una contrasena.");
        return;

    }else if( pass1 != pass2 ){
        alert("Las contrasenas no coinciden.");
        return;

    }else{
        this.submit();
    }
    
})


