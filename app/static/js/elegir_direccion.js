$('#selector').click(function(){
    $('#comprar1').attr('disabled', false)
    let elegido = $('#selector').val()
    $('#comprar').attr('href', elegido)
})

$('#comprar1').click(function(){
    $('#modal').fadeIn();
})

$('#no').click(function(){
    $('#modal').fadeOut();
});

$('#cerrar').click(function(){
    $('#modal').fadeOut();
});