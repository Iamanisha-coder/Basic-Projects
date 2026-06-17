const displayEl = document.getElementById('password-display');
const lengthEl = document.getElementById('length');
const uppercaseEl = document.getElementById('uppercase');
const numbersEl = document.getElementById('numbers');
const symbolsEl = document.getElementById('symbols');
const generateBtn = document.getElementById('generate-btn');

const lowercaseChars = "abcdefghijklmnopqrstuvwxyz";
const uppercaseChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const numberChars = "0123456789";
const symbolChars = "!@#$%^&*()_+~`|}{[]:;?><,./-=";

function generatePassword() {
    let length = parseInt(lengthEl.value);
    let charPool = lowercaseChars;

    if (uppercaseEl.checked) charPool += uppercaseChars;
    if (numbersEl.checked) charPool += numberChars;
    if (symbolsEl.checked) charPool += symbolChars;

    if (charPool === "") {
        displayEl.innerText = "Select at least 1 option";
        return;
    }

    let password = "";
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * charPool.length);
        password += charPool[randomIndex];
    }

    displayEl.innerText = password;
}

generateBtn.addEventListener('click', generatePassword);
