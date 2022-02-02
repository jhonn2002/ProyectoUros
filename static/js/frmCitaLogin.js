
function alertaTrue() {
    sweetAlert({
        title:'¡Correcto!!',
        text: $("#txtMensajeS").val(),
        type:'success'
    },function(isConfirm){
        red()
    });
}

function alertaFalse() {
    sweetAlert({
        title:'Problemas!!',
        text: $("#txtMensajeS").val(),
        type:'warning'
    },function(isConfirm){
        red()
    });
}

function alertaTrueTrabaje() {
    sweetAlert({
        title:'¡Correcto!!',
        text: $("#txtMensajeS").val(),
        type:'success'
    },function(isConfirm){
        redTrabaje()
    });
}

function alertaFalseTrabaje() {
    sweetAlert({
        title:'Problemas!!',
        text: $("#txtMensajeS").val(),
        type:'warning'
    },function(isConfirm){
        redTrabaje()
    });
}

function alertaTrueChequeo() {
    sweetAlert({
        title:'¡Correcto!!',
        text: $("#txtMensajeS").val(),
        type:'success'
    },function(isConfirm){
        redChequeo()
    });
}

function alertaFalseChequeo() {
    sweetAlert({
        title:'Problemas!!',
        text: $("#txtMensajeS").val(),
        type:'warning'
    },function(isConfirm){
        redChequeo()
    });
}

function alertaTruePqr() {
    sweetAlert({
        title:'¡Correcto!!',
        text: $("#txtMensajeS").val(),
        type:'success'
    },function(isConfirm){
        redPqr()
    });
}

function alertaFalsePqr() {
    sweetAlert({
        title:'Problemas!!',
        text: $("#txtMensajeS").val(),
        type:'warning'
    },function(isConfirm){
        redPqr()
    });
}

function alertaTrueAsociacion() {
    sweetAlert({
        title:'¡Correcto!!',
        text: $("#txtMensajeS").val(),
        type:'success'
    },function(isConfirm){
        redAsoci()
    });
}

function alertaFalseAsociacion() {
    sweetAlert({
        title:'Problemas!!',
        text: $("#txtMensajeS").val(),
        type:'warning'
    },function(isConfirm){
        redAsoci()
    });
}

function red() {
    window.location.href = '/citaLogin';
}

function redTrabaje() {
    window.location.href = '/trabajeConNosotros';
}
function redChequeo() {
    window.location.href = '/chequeoEjecutivo';
}
function redPqr() {
    window.location.href = '/formPqr';
}

function redAsoci() {
    window.location.href = '/derechosDeberes';
}