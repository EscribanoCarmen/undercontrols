$('#id_num_tarjeta').attr('placeholder', '16 dígitos');
$('#id_num_tarjeta').attr('pattern', '^[0-9]{16}$')
$('#id_fecha_caducidad').attr('placeholder', 'Ej: 03/22 (mes/año)');
$('#id_fecha_caducidad').attr('pattern', '^(|[0-2][1-9])\/([0-9]{2})$');
$('#id_codigo_seguridad').attr('placeholder', '3 dígitos');
$('#id_codigo_seguridad').attr('pattern', '^[0-9]{3}$')