import country_list from "./country.js";

const droplist = document.querySelectorAll(".drop-list select");
let fromCurrency = document.querySelector(".from select");
let toCurrency = document.querySelector(".to select");
const getButton = document.querySelector("#btn");

for (let i = 0; i < droplist.length; i++) {
   for(let currency_code in country_list){
         // selectiong USD to INR by defeault
         let selected;
         if(i == 0){
            selected = currency_code == "USD" ? "selected" : "";
         }
         else if(i == 1){
            selected = currency_code == "INR" ? "selected" : "";
         }
         // creating option tag
        let optionsTag = `<option value="${currency_code}" ${selected}>${currency_code}</option>`;
         // inserting option tag inside select tag
        droplist[i].insertAdjacentHTML("beforeend", optionsTag);
   }
   // changing flag 
   droplist[i].addEventListener("change", e =>{
      loadFlag(e.target);
   })
}

// changeing flag function...
function loadFlag(element){
   for(let code in country_list){
      if(code == element.value){
         let imgTag = element.parentElement.querySelector("img");
         imgTag.src = `https://flagcdn.com/32x24/${country_list[code].toLowerCase()}.png`;
      }
   }
}

// get exchange rate function
getButton.addEventListener("click", e=>{
   e.preventDefault();
   getExchangeRate();
});

function getExchangeRate(){
   const amt = document.querySelector(".amount input");
   const exchangeRateTxt = document.querySelector(".exchange-rate");
   let amountVal = amt.value;

   if(amountVal == "" || amountVal == "0"){
      amt.value = "1";
      amountVal = 1;
   }
   exchangeRateTxt.innerText = "Getting exchange rate...";
   let url = `https://v6.exchangerate-api.com/v6/1ea79d4c84d15c3054c36a00/latest/${fromCurrency.value}`;
   fetch(url).then(response => response.json()).then(result => {
      let exchangeRate = result.conversion_rates[toCurrency.value];
      let totalExchangeRate = (amountVal * exchangeRate).toFixed(2);
      exchangeRateTxt.innerText = `${amountVal} ${fromCurrency.value}= ${totalExchangeRate} ${toCurrency.value}`;
   }).catch(() =>{
      exchangeRateTxt.innerText = "Something went wrong..."
   });
}

// exchange icon function
const exchangeIcon = document.querySelector(".drop-list .icon");
exchangeIcon.addEventListener("click", () => {
   let tempCode = fromCurrency.value;
   fromCurrency.value = toCurrency.value;
   toCurrency.value = tempCode;
   getExchangeRate();
   loadFlag(fromCurrency);
   loadFlag(toCurrency);
})