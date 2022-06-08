let precioBase = parseInt($('#id_precio').val(), 10);
let extraBotones = false; let botones = 100;
let extraCuero = false; let cuero = 200;
let extraAlcantara = false; let alcantara = 150;
let extraGoma = false; let goma = 100;
let extraIntermitente = false; let intermitente = 50;
let extraLuces = false; let luces = 50;
$('#id_botones').attr('disabled', 'disabled');
$('#id_intermitentes').attr('disabled', 'disabled');
$('#id_luces').attr('disabled', 'disabled');

$('#id_piel_aro').click(function () {
    $('#id_botones').attr('disabled', false);
    $('#id_intermitentes').attr('disabled', false);
    $('#id_luces').attr('disabled', false);
    if(extraAlcantara){
        precioBase -= alcantara;
    }

    if(extraCuero){
        precioBase-= cuero;
    }

    if(extraGoma){
        precioBase -= goma;
    }

    if ($("#id_piel_aro option:selected").text() == "Cuero") {
        $("#imagen-1").fadeToggle();
        precioBase += cuero;
        $('#id_precio').val(precioBase);
        $('#precio-vivo').text(precioBase + ",00€");
        extraCuero = true;
        extraAlcantara = false;
        extraGoma = false;
    }
    if ($("#id_piel_aro option:selected").text() == "Alcántara") {
        $("#imagen-3").fadeToggle();
        precioBase += alcantara;
        $('#id_precio').val(precioBase);
        $('#precio-vivo').text(precioBase + ",00€");
        extraCuero = false;
        extraAlcantara = true;
        extraGoma = false;
    }
    if ($("#id_piel_aro option:selected").text() == "Goma") {
        $("#imagen-2").fadeToggle();
        precioBase += goma;
        $('#id_precio').val(precioBase);
        $('#precio-vivo').text(precioBase + ",00€");
        extraCuero = false;
        extraAlcantara = false;
        extraGoma = true;
    }
});

$('#id_botones').click(function () {
    if(extraBotones){
        precioBase -= botones;
    }

    if($('#id_botones option:selected').text() == "4"){
        $('.botones-4').fadeToggle();
        precioBase += botones;
        $('#id_precio').val(precioBase);
        $('#precio-vivo').text(precioBase + ",00€");
        extraBotones = true;
    }

    if($('#id_botones option:selected').text() == "0"){
        $('#id_precio').val(precioBase);
        $('#precio-vivo').text(precioBase + ",00€");
        extraBotones = false;
    }
});

$('#id_intermitentes').click(function () {
    if ($('#id_intermitentes').prop('checked')) {
        $('#intermitente').fadeIn();
        precioBase += intermitente;
        $('#id_precio').val(precioBase);
        $('#precio-vivo').text(precioBase + ",00€");
    } else {
        $('#intermitente').fadeOut();
        precioBase -= intermitente;
        $('#id_precio').val(precioBase);
        $('#precio-vivo').text(precioBase + ",00€");
    }
});

$('#id_luces').click(function () {
    if ($('#id_luces').prop('checked')) {
        $('#luces').fadeIn();
        precioBase += luces;
        $('#id_precio').val(precioBase);
        $('#precio-vivo').text(precioBase + ",00€");
    } else {
        $('#luces').fadeOut();
        precioBase -= luces;
        $('#id_precio').val(precioBase);
        $('#precio-vivo').text(precioBase + ",00€");
    }
});