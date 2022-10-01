// error notifications

const notificationDetailByError = new Map();

notificationDetailByError.set("Invalid credentials.", {
    imageUrl: "/static/assets/invalid-login.jpeg",
    imageWidth: 500,
    imageHeight: 800,
    timer: 4000,
});

notificationDetailByError.set("Invalid sign up credentials.", {
    imageUrl: "/static/assets/invalid-sign-up.jpeg",
    imageWidth: 500,
    imageHeight: 800,
});

notificationDetailByError.set("Profile update has failed.", {
    imageUrl: "/static/assets/invalid-profile-update.jpeg",
    imageWidth: 500,
    imageHeight: 800,
    timer: 12000,
});

notificationDetailByError.set("Password update has failed.", {
    imageUrl: "/static/assets/invalid-password-update.jpeg",
    imageWidth: 500,
    imageHeight: 800,
    timer: 12000,
});

const errorNotificationDetailDueTo = errorDescription => {
    return {
        icon: 'error',
        title: 'Oops...',
        text: errorDescription
    }
}

// success notifications

const notificationDetailByInfo = new Map();

notificationDetailByInfo.set("Sign up has been successful", {
    imageUrl: "/static/assets/successful-signup.jpeg",
    imageWidth: 500,
    imageHeight: 800,
    timer: 4000,
});

notificationDetailByInfo.set("Profile has been successfully updated", {
    imageUrl: "/static/assets/successful-profile-update.jpeg",
    imageWidth: 500,
    imageHeight: 800,
    timer: 4000,
});

notificationDetailByInfo.set("Password has been successfully updated", {
    imageUrl: "/static/assets/successful-password-update.jpeg",
    imageWidth: 500,
    imageHeight: 800,
    timer: 4000,
});

const infoNotificationDetailDueTo = infoDescription => {
    return {
        icon: 'success',
        title: 'Great!',
        text: infoDescription
    }
}

const getMessageInformation = () => {
    const messageErrorElements = document.getElementsByClassName("message-error");
    const messageInfoElements = document.getElementsByClassName("message-info");

    if (messageErrorElements[0] != null) {
        const element = messageErrorElements[0];
        const message = element.textContent;
        element.remove();
        const notificationDetail =
            notificationDetailByError.has(message)
                ? notificationDetailByError.get(message)
                : errorNotificationDetailDueTo(message);
        Swal.fire(notificationDetail);
    }

    if (messageInfoElements[0] != null) {
        const element = messageInfoElements[0];
        const message = element.textContent;
        element.remove();
        const notificationDetail =
            notificationDetailByInfo.has(message)
                ? notificationDetailByInfo.get(message)
                : infoNotificationDetailDueTo(message);
        Swal.fire(notificationDetail);
    }
}

window.addEventListener("load", getMessageInformation);
