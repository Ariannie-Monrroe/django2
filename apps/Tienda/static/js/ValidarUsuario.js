const formulario = document.getElementById("formValidation");

formulario.addEventListener('submit',function(evento){
    evento.preventDefault();

    if (document.getElementById("emailNuevoId").value.length == 0) {
        alert("Ingrese el correo.");
        return;
    }else if (document.getElementById("usernameNuevoId").value.length == 0){
        alert("Ingrese el Nombre.");
        return;
        
    }else if (document.getElementById("passwordNuevoId").value.length == 0){
        alert("Ingrese la contrasena.");
        return;

    }else if(document.getElementById("passwordNuevaValidarId").value == document.getElementById("passwordNuevaValidar").value){
        alert("Las contrasenas no coinciden.");
        return;

    }else{
        this.submit();
    }
})


