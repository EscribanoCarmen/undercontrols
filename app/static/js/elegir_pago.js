$('#selector').click(function(){
    let elegido = $('#selector').val()
    $('#pasar').attr('href', elegido);
    $('#pasar').css('opacity', '1');
})
