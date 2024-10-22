document.addEventListener("DOMContentLoaded", function() {
    const inputs = document.querySelectorAll("input[type='text'], input[type='phone'], input[type='email']");

    inputs.forEach(input => {
        input.addEventListener("focus", function() {
            input.style.borderColor = "red";
        });

        input.addEventListener("blur", function() {
            input.style.borderColor = "white";
        });
    });
});