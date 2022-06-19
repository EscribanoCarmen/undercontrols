let precioBase = parseInt($('#id_precio').val(), 10);
let extraBotones8 = false; let botones8 = 50;
let extraBotones15 = false; let botones15 = 100;
//_________________
let extraLevas2 = false; let levas2 = 50;
let extraLevas3 = false; let levas3 = 150;
let extraLevas4 = false; let levas4 = 200;
//________________
let extraMaterial = false;
let extraDisplay = false; let display = 200;

//BOTONES ******************
$("#id_botones").click(function () {
    //comprobar si ya se ha elegido antes unos botones
    if (extraBotones15) {
        precioBase -= botones15;
    }
    if (extraBotones8) {
        precioBase -= botones8;
    }
    if ($("#id_botones option:selected").text() == "8 [+50€]") {
        $('.seccion-10').fadeToggle();
        //compruebo si ha elegido antes los otros, para restarle su precio
        precioBase += botones8;
        $('#id_precio').val(precioBase);
        $('#precio-vivo').text(precioBase + ",00€");
        extraBotones8 = true;
        extraBotones15 = false;

    }
    if ($("#id_botones option:selected").text() == "15 [+100€]") {
        $('.seccion-10').fadeToggle();
        $('.seccion-13').fadeToggle();

        precioBase += botones15;
        $('#id_precio').val(precioBase);
        $('#precio-vivo').text(precioBase + ",00€");
        extraBotones15 = true;
        extraBotones8 = false;
    }

});

//LEVAS ********************
$('#id_numero_levas').click(function () {
    if (extraLevas2) {
        precioBase -= levas2;
    }
    if (extraLevas3) {
        precioBase -= levas3;
    }
    if (extraLevas4) {
        precioBase -= levas4;
    }
    if ($('#id_numero_levas option:selected').text() == "2 [+50€]") {
        $('.levas-2').fadeToggle();
        precioBase += levas2;
        $('#id_precio').val(precioBase);
        $('#precio-vivo').text(precioBase + ",00€");
        extraLevas2 = true;
        extraLevas3 = false;
        extraLevas4 = false;
    }
    if ($('#id_numero_levas option:selected').text() == "3[+150€]") {
        $('.levas-2').fadeToggle();
        $('#embrague').fadeToggle();
        precioBase += levas3;
        $('#id_precio').val(precioBase);
        $('#precio-vivo').text(precioBase + ",00€");
        extraLevas2 = false;
        extraLevas3 = true;
        extraLevas4 = false;
    }

    if ($('#id_numero_levas option:selected').text() == "4 [+200€]") {
        $('.levas-2').fadeToggle();
        $('#embrague').fadeToggle();
        $('#embrague-aux').fadeToggle();
        precioBase += levas4;
        $('#id_precio').val(precioBase);
        $('#precio-vivo').text(precioBase + ",00€");
        extraLevas2 = false;
        extraLevas3 = false;
        extraLevas4 = true;
    }
})

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
        $('#display').fadeIn();
        precioBase += display;
        $('#id_precio').val(precioBase);
        $('#precio-vivo').text(precioBase + ",00€");
    } else {
        $('#display').fadeOut();
        precioBase -= display;
        $('#id_precio').val(precioBase);
        $('#precio-vivo').text(precioBase + ",00€");
    }
});