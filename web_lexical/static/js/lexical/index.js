$(document).on('submit','#login-form',function(e){
    e.preventDefault();
    console.log("hellow owlr")
    console.log($('#username').val())
    console.log($('#password').val())
    console.log($('input[name=csrfmiddlewaretoken]').val())
    $.ajax({
        type:'POST',
        url:login_url,
        data:
        {
            username:$('#username').val(),
            password:$('#password').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(data){
            if (!data["valid"]) {
                $("#login-form").trigger('reset');
                alert("Username or password is incorrect");
            } else {
                document.location.href = url_status;
            }
        }
    })
});