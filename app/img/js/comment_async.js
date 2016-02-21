function parse_data(full_name, body) {
    return '<div class="panel panel-default"> <div class="panel-heading"><b>' + full_name + '</b> <small class="pull-right"> 0 minutes</small></div> <div class="panel-body">' + body + '</div> </div>';

}
$('#formComment').validate({
    rules:{
        full_name:{
            required: true
        },
        user_email: {
            required: true,
            email: true
        },
        comment_body:{
            required: true
        }

    },
    submitHandler: function(form){
        $.ajax({
            method: "POST",
            url: $('#post_url').val(),
            data: {
                full_name: $('#full_name').val(),
                email: $('#user_email').val(),
                body: $('#comment-body').val(),
                home_id: $('#home_id').val()
            }
         })
            .done(function(e){
                var html = parse_data($('#full_name').val(), $('#comment-body').val());
                $('.reviews-list').prepend(html);
                $('#full_name').val("");
                $('#user_email').val("");
                $('#comment-body').val("")
            })
    }
});