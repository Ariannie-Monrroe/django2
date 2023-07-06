const formulario = document.getElementById("formularioAgregar");

formulario.addEventListener('submit',function(evento){
    evento.preventDefault();

    if (document.getElementById("txtSku").value.length == 0) {
        alert("Ingrese el codigo del producto.");
        return;
    }else{
        this.submit();
    }
})