
window.addEventListener("load", getMessageInformation);

function getMessageInformation(){
    let messages_error = document.getElementsByClassName("message-error");

    let messages_ok = document.getElementsByClassName("message-info");


if (messages_error[0] != null){

    let message_error =  messages_error[0].textContent

    if(message_error === 'Invalid credentials.'){
        Swal.fire({
        imageUrl: '/static/assets/invalid-login.jpeg',
        imageWidth: 500,
        imageHeight: 800,
        timer: 4500
    })
    }
}
}

