
function alertaTrue() {
    sweetAlert({
        title:'¡Correcto!!',
        text: $("#txtMensaje").val(),
        type:'success'
    },function(isConfirm){
        red()
    });
}

function alertaFalse() {
    sweetAlert({
        title:'Problemas!!',
        text: $("#txtMensaje").val(),
        type:'warning'
    },function(isConfirm){
        red()
    });
}

function red() {
    window.location.href = '/oficina';
}