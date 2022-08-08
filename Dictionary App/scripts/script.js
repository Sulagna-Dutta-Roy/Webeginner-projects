let searchForm = document.getElementById("searchForm");
searchForm.addEventListener("submit", (event) => {

  event.preventDefault(); // To prevent page from reloading

  const xhr = new XMLHttpRequest();

  let searchBox = document.getElementById("searchBox").value;

  xhr.open("GET", `https://api.dictionaryapi.dev/api/v2/entries/en/${searchBox}`, true);

  xhr.onload = function () {
    if (xhr.status === 200) {
      const dictionaryObj = JSON.parse(this.responseText);
      
      document.getElementById("wordHeader").innerHTML = `<strong>${searchBox}</strong>`; // Adding search text

      let str = "";
      for (const key in dictionaryObj[0].meanings[0].definitions) {
        str += `<li>${dictionaryObj[0].meanings[0].definitions[key].definition}</li>`; // Adding definitions
      }
      document.getElementById("wordDefinition").innerHTML = str;
    }
  };

  xhr.send();

  searchForm.reset(); // To clear the form
});
