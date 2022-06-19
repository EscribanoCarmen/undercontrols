let precioBase = parseInt($('#id_precio').val(), 10);
let extraBotones8 = false; let botones8 = 100;
let extraBotones14 = false; let botones14 = 170;
//_________________
let extraLevas0 = false; let levas0 = 0;
let extraLevas2 = false; let levas2 = 100;
//________________
let extraMaterial = false;
let extraDisplay = false; let display = 200;
$('#id_material_levas').attr('disabled', 'disabled')

$("#id_botones").click(function () {
    if (extraBotones14) {
        precioBase -= botones14;
    }
    if (extraBotones8) {
        precioBase -= botones8;
    }
    if ($("#id_botones option:selected").text() == "8 [+100€]") {
        $('.botones-8').fadeToggle();
        //compruebo si ha elegido antes los otros, para restarle su precio
        precioBase += botones8;
        $('#id_precio').val(precioBase);
        $('#precio-vivo').text(precioBase + ",00€");
        extraBotones8 = true;
        extraBotones14 = false;

    }
    if ($("#id_botones option:selected").text() == "14 [+170€]") {
        $('.botones-8').fadeToggle();
        $('.botones-14').fadeToggle();

        precioBase += botones14;
        $('#id_precio').val(precioBase);
        $('#precio-vivo').text(precioBase + ",00€");
        extraBotones14 = true;
        extraBotones8 = false;
    }

});

//LEVAS
$('#id_numero_levas').click(function () {
    if (extraLevas2) {
        precioBase -= levas2;
    }
    if ($('#id_numero_levas option:selected').text() == "2 [+100€]") {
        $('.levas-2').fadeToggle();
        precioBase += levas2;
        $('#id_precio').val(precioBase);
        $('#precio-vivo').text(precioBase + ",00€");
        extraLevas2 = true;
        $('#id_material_levas').attr('disabled', false)
    }
    if ($('#id_numero_levas option:selected').text() == "0 [+0€]") {
        if (extraLevas2) {
        $('#id_precio').val(precioBase);
        $('#precio-vivo').text(precioBase + ",00€");
        extraLevas2 = false;
        $('#id_material_levas').attr('disabled', 'disabled')
    }
}
});



$('#id_material_levas').click(function () {
    if (extraMaterial) {
        precioBase -= 50;
    }
    if ($('#id_material_levas option:selected').text() == "Plástico [+0€]") {
        $('.levas').css('background-color', 'rgb(62, 62, 62)');

        extraMaterial = false;
    } else if ($('#id_material_levas option:selected').text() == "Metal [+50€]") {
        $('.levas').css('background-color', 'rgb(25, 25, 25)');
        precioBase += 50;
        extraMaterial = true;
    }
    $('#id_precio').val(precioBase);
    $('#precio-vivo').text(precioBase + ",00€");
});


$('#id_display').click(function () {
    if ($('#id_display').prop('checked')) {
        $('#dashboard').fadeIn();
        precioBase += display;
        $('#id_precio').val(precioBase);
        $('#precio-vivo').text(precioBase + ",00€");
    } else {
        $('#dashboard').fadeOut();
        precioBase -= display;
        $('#id_precio').val(precioBase);
        $('#precio-vivo').text(precioBase + ",00€");
    }
});
