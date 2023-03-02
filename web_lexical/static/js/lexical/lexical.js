$('#add-dict').on('submit', function(e){
    e.preventDefault();
    console.log(url_lexical)
    $.ajax({
        type:'POST',
        url:url_lexical,
        data:
        {
            word:$('#word').val(),
            typeOfWord:$('#wordtype').val(),
            meaning:$('#meaning').val(),
        },
        success:function(data){
            if (!data['valid']) {
                alert(data["error"]);
                document.getElementById("add-dict").reset();
            } else {
                alert(data["ok"]);
                location.reload();
            }
        }
    })
});