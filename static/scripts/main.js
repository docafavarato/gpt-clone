$(document).ready(function() {
    var answer = $("#answer");
    var answerText = answer.text();
    answer.empty();
    var i = 0;
    var typingEffect = setInterval(function() {
        answer.append(answerText.charAt(i));
        i++;
        if (i > answerText.length) {
            clearInterval(typingEffect);
        }
    }, 15);
});
