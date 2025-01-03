// Get the redirect URL from the anchor tag's href attribute
const redirectLink = document.getElementById('redirect-link');
const redirectUrl = redirectLink.href;

// Set the initial countdown value in seconds
let countdown = 4; 
const countdownSpan = document.getElementById('countdown');
const countdownInterval = setInterval(updateCountdown, 1000); // update every 1 second

function updateCountdown() {
    if (countdown === 0) {
        clearInterval(countdownInterval); // stop the interval
        window.location.href = redirectUrl; // Redirect using the obtained URL
    } else {
        countdownSpan.textContent = countdown; // update the countdown display
        countdown--; // decrement the countdown
    }
}
