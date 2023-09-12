const $formulario = document.getElementById('electro');
const $productoTxt = document.getElementById('Producto');
const $marcatxt = document.getElementById('marca');
const $stocktxt = document.getElementById('stock');
const $preciotxt = document.getElementById('precio');
$mensaje = "";

const botonesEliminar = document.querySelectorAll('.btnEliminar');

(function(){
    $formulario.addEventListener('submit',function(e){
        let nombre = String($productoTxt.value).trim();
        if (nombre.length===0){
            $mensaje = "Producto Obligatorio";
            document.getElementById('msgProducto').classList.add('text-danger');
            document.getElementById('msgProducto').innerHTML = $mensaje;
            e.preventDefault();
        }else{
            document.getElementById('msgProducto').innerHTML = "";
        }  
    });
    $formulario.addEventListener('submit',function(e){
        let nombre = String($marcatxt.value).trim();
        if (nombre.length===0){
            $mensaje = "Marca Obligatorio";
            document.getElementById('msgmarca').classList.add('text-danger');
            document.getElementById('msgmarca').innerHTML = $mensaje;
            e.preventDefault();
        }else{
            document.getElementById('msgmarca').innerHTML = "";
        }  
    });
    $formulario.addEventListener('submit',function(e){
        let nombre = String($stocktxt.value).trim();
        if (nombre.length===0){
            $mensaje = "Stock Obligatorio";
            document.getElementById('msgstock').classList.add('text-danger');
            document.getElementById('msgstock').innerHTML = $mensaje;
            e.preventDefault();
        }else{
            document.getElementById('msgstock').innerHTML = "";
        }  
    });
    $formulario.addEventListener('submit',function(e){
        let nombre = String($preciotxt.value).trim();
        if (nombre.length===0){
            $mensaje = "Precio Obligatorio";
            document.getElementById('msgprecio').classList.add('text-danger');
            document.getElementById('msgprecio').innerHTML = $mensaje;
            e.preventDefault();
        }else{
            document.getElementById('msgprecio').innerHTML = "";
        }  
    });

    botonesEliminar.forEach(boton =>{
        boton.addEventListener('click',function(e){
            e.preventDefault();
            Swal.fire({
                title: "¿Estas seguro de eliminarlo?",
                showCancelButton: true,
                confirmButtonText: "Eliminar Registro",
                cancelButtonText: "conservarlo",
                confirmButtonColor: '#d00',
                cancelButtonColor: '#0c17b4',
                backdrop: true,
                preConfirm: () => {
                    location.href = e.target.href;
                },
                allowOutsideClick: () => false,
                allowEscapeKey: ()  => false,
            });
        });
    });

})();


