const quoteEl = document.querySelector('.quote');
const personEl = document.querySelector('.person');
const btnEl = document.querySelector('.generator');

const url = "https://api.quotable.io/random?minLength=70&maxLength=120";


let getQuote = () =>{
    fetch(url)
        .then((data) => data.json())
        .then((item) =>{
            quoteEl.textContent = `"${item.content}"`;
            personEl.textContent = `-${item.author}`;
    })
}

btnEl.addEventListener('click',getQuote);
