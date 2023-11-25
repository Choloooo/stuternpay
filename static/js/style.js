const send =document.getElementById("amountToSend");
const recieve =document.getElementById("amountToReceive");
const send_currency =document.getElementById("currencyToSend");
const exchange_rate= document.getElementById("exchangeRate");



function calculate(params) {
    const currency1 = send.value;
    const currency2 = send.value;

    fetch(`http://api.exchangeratesapi.io/v1/latest?access_key=a12c21ed50819538991fcc740c96833e/latest/${currency1}`).then((res) => res.json()
    .then((data) => {
        const rate = data.conversion_rate[currency2];
        theRate.innerHtml = `1 ${currency1} =${rate}  ${currency2}`;
        recieve.value = (send.value * rate).toFixed(2)
    }));
    send_currency.addEventListener("change", calculate);
    send.addEventListener("input", calculate);
    recieve.addEventListener("input", calculate);
    swap.addEventListener("click", () => {
    const flash = send_currency.value;
    send_currency.value = send_currency.value;
    c2.value = flash;
    calculate();
    })}