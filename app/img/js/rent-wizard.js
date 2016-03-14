$('#sendWizard').click(function (e) {

    e.preventDefault();
    $.ajax({
            method: "POST",
            url: $('#post_urlWizard').val(),
            data: {
                fname: $('#Fname').val(),
                lname: $('#Lname').val(),
                wphone: $('#wphone').val(),
                email: $('#Wemail').val(),
                country: $('#country').val(),
                city: $('#city').val(),
                cantHabitaciones: $('#cantHabitaciones').val(),
                cantSimples: $('#cantSimples').val(),
                cantDobles: $('#cantDobles').val(),
                cantTriples: $('#cantTriples').val(),
                desde: $('#desde').val(),
                hasta: $('#hasta').val(),
                llegar: $('#llegar').val(),
                horaLLegada: $('#clock').val(),
                informacionCliente: $('#informacionCliente').val()

            }
        })
        .done(function () {

            console.log(data);
        });
});
