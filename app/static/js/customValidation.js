var users, clients;

$.when(
    $.getJSON('/api/users', function(response) {
        users = response;
    }),
    $.getJSON('/api/clients', function(response) {
        clients = response;
    })
).then(function() {

    $.validator.addMethod('used', function(value, element) {

        var exist = true;

        users.forEach(function(user) {

            if (value === user.username ||
                value === user.email) {
                exist = false;
                return;
            }
        });

        return exist;
    });

    $.validator.addMethod('clients', function(value, element) {

    	var exist = false;

    	users.forEach(function(user) {
    		if ( user.dni === value ) exist = true;
    	});

    	if ( !exist ) return true;

        var isClient = false;

        clients.forEach(function(client) {
            if (value === client.clientDni) {
                isClient = true;
                return;
            }
        });

        return isClient;
    });

});