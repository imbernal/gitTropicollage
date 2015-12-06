function parse_data(full_name, body) {
    return '<div class="panel panel-default"> <div class="panel-heading"><b>' + full_name + '</b> <small class="pull-right"> 0 minutes</small></div> <div class="panel-body">' + body + '</div> </div>';

}

$('input[value="Comment"]').click(function (e) {
    e.preventDefault();
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
        .done(function () {
            var html = parse_data($('#full_name').val(), $('#comment-body').val());
            $('.reviews-list').prepend(html);
        })
        .error(function () {
            console.log("Oops");
        });
});