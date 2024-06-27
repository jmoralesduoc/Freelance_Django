$(document).ready(function(){
    var monedas = ["uf", "ivp", "dolar", "dolar_intercambio", "euro", "ipc", "utm", "imacec", "tpm", "libra_cobre", "tasa_desempleo", "bitcoin"];

    // Obtener la fecha actual del sistema
    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0'); // Enero es 0
    var yyyy = today.getFullYear();
 
    var fecha = dd + '-' + mm + '-' + yyyy;

    $("#fechaSistema").text(fecha);
    // Crear la cabecera de la tabla una sola vez
    $("#tipocambio").append("<tr> <th> Tipo Cambio </th> <th> Valor </th> </tr>");

    $.each(monedas, function(index, moneda){
        $.get("https://mindicador.cl/api/" + moneda + "/" + fecha, function(data){
            $.each(data.serie, function(i, item){
                $("#tipocambio").append("<tr> <td>" + data.nombre + "</td> <td> $" + item.valor + "</td> </tr>");
            });
        });
    });
});
