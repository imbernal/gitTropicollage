
$('input[value="Submit"]').click(function(e){
    e.preventDefault();

    $.ajax({
        method: "POST",
        url: $('#wizard_url').val(),
        data:{
            fname : $('fname').val(),
            lname : $('lname').val(),
            wphone: $('wphone').val(),
            email: $('email').val(),
            country: $('country').val(),
            city: $('city').val(),
            cantHabitaciones: $('cantHabitaciones').val(),
            cantSimples: $('cantSimples').val(),
            cantDobles: $('cantDobles').val(),
            cantTriples: $('cantTriples').val(),
            desde: $('desde').val(),
            hasta: $('hasta').val(),
            medioLLegada: $('medioLLegada').val(),
            horaLLegada: $('horaLLegada').val(),
            imformacionCliente: $('imformacionCliente').val()
        }
    })
        .done(function(){
            console.log(data.cantSimples);
        });
});
