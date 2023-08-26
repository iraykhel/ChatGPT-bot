const inputElem = document.getElementById('user_input');
const chatboxElem = document.getElementById('chatbox');
const history = [['assistant',"What's up?"]]

inputElem.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        let userMessage = inputElem.value;
        chatboxElem.innerHTML += "<div class='req'>"+userMessage + "<div>";
        history.push(['user',userMessage])

        fetch('/ask', {
            method: 'POST',
            body: JSON.stringify({'history': history}),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            history.push(['assistant',data.bot_response])
            chatboxElem.innerHTML += "<div class='resp'>"+data.bot_response + "<div>";
            chatboxElem.scrollTop = chatboxElem.scrollHeight;
        });

        inputElem.value = "";
    }
});