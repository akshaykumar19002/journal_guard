var message_timeout = document.getElementById("message-timer");

setTimeout(() => {
    if (message_timeout)
        message_timeout.style.display = "none";
}, 2500);

function setTimezoneCookie() {
    let timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
    console.log("Timezone: " + timezone)
    document.cookie = "timezone=" + timezone + ";path=/;";
}

window.onload = function () {
    console.log("Setting timezone cookie");
    setTimezoneCookie();
}
