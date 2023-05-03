$(document).ready(function() {
    var answer = $(".container-answer");
    var answerText = answer.html();
    answer.empty();
    var i = 0;
    var typingEffect = setInterval(function() {
        answer.html("<p>" + answerText.substr(0, i) + "</p>");
        i++;
        if (i > answerText.length) {
            clearInterval(typingEffect);
        }
    }, 10);
});


$(document).ready(function() {
    $('body').on('click', '#clipboard', function(event) {
        event.stopPropagation(); 
        var answerText = document.getElementById("answerText");

        navigator.clipboard.writeText(answerText.innerText)
            .then(() => console.log("Texto copiado para a área de transferência"))
            .catch(err => console.error("Erro ao copiar o texto: ", err));
    });
});


$(document).ready(function() {
    $("#ask").click(function(e) {
        $(".alert").fadeIn("slow");
    });
});

$(document).ready(function() {
    $("#create_image").click(function(e) {
        $(".alert").fadeIn("slow");
    });
});
