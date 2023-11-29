document.addEventListener('DOMContentLoaded', function() {
  const c1 = document.getElementById("currency-one");
  const c2 = document.getElementById("currency-two");
  const amount1 = document.getElementById("amount-one");
  const amount2 = document.getElementById("amount-two");
  const swap = document.getElementById("swap");
  const theRate = document.getElementById("rate");

  // Fetch exchange rate from the API
  function calculate() {
    const curr1 = c1.value;
    const curr2 = c2.value;
    fetch(
      `http://api.exchangeratesapi.io/v1/latest?access_key=2086b93621b88d5679f91ad614d8e0bb${curr1}`
    )
      .then((res) => res.json())
      .then((data) => {
        // console.log(data);
        // Updating the data
        const rate = data.conversion_rates[curr2];
        theRate.innerText = `1 ${curr1} = ${rate} ${curr2}`;
        amount2.value = (amount1.value * rate).toFixed(2);
      });
  }

  // Event  Listeners
  c1.addEventListener("change", calculate);
  amount1.addEventListener("input", calculate);
  c2.addEventListener("change", calculate);
  amount2.addEventListener("input", calculate);
  swap.addEventListener("click", () => {
    const flash = c1.value;
    c1.value = c2.value;
    c2.value = flash;
    calculate();
  });

  // Initial calculation when the page is loaded
  calculate();
});
