$(function(){

    $(document).on('change','#selecRolIndex',function() {
        var rol = $("#selecRolIndex").val();
        if (rol == 1) {
            window.location.href = '/rol?idRol='+rol+''; 
        }else
            if (rol == 2) {
                window.location.href = '/rol?idRol='+rol+''; 
            }
    });
    
});

function clickFoto(n) {
    $("#imgCanguro").attr("src","static/fotos/fotos_inicio/"+n+"");
    $('#myModal').modal('show');
}


