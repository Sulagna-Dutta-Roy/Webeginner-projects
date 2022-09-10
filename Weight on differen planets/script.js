const planets = document.getElementById("planets");
const input = document.getElementById("weight");
const result = document.querySelector(".answer");
const planetNames = document.querySelectorAll("option");
const btn = document.querySelector("button");
const img = document.querySelector(".image");

function clear() {
  input.value = "";
  result.innerHTML = "";
  img.innerHTML = "";
}

btn.addEventListener("click", () => {
  let text = planets.options[planets.selectedIndex].text;
  let value = "";
  let imgSrc = "";
  if (!input.value) return;

  switch (text) {
    case "Mercury":
      value = Math.trunc(input.value * 0.38);
      imgSrc = "images/Mercury.png";
      break;
    case "Venus":
      value = Math.trunc(input.value * 0.91);
      imgSrc = "images/Venus.png";
      break;
    case "Earth":
      value = input.value * 1.0;
      imgSrc = "images/Earth.png";
      break;
    case "Mars":
      value = input.value * 0.38;
      imgSrc = "images/Mars.png";
      break;
    case "Jupiter":
      value = Math.trunc(input.value * 2.34);
      imgSrc = "images/Jupiter.png";
      break;
    case "Saturn":
      value = Math.trunc(input.value * 1.06);
      imgSrc = "images/Saturn.png";
      break;
    case "Uranus":
      value = Math.trunc(input.value * 0.92);
      imgSrc = "images/Uranus.png";
      break;
    case "Neptune":
      value = Math.trunc(input.value * 1.19);
      imgSrc = "images/Neptune.png";
      break;
    default:
      return;
  }

  let markUp = `
  <p>The weight is ${value} kgs</p>`;
  result.insertAdjacentHTML("beforeend", markUp);

  let markUp2 = `
  <img id="planet-img" src=${imgSrc} alt="" />`;
  img.insertAdjacentHTML("beforeend", markUp2);
});

input.addEventListener("click", clear);

planets.addEventListener("click", () => {
  img.innerHTML = "";
  result.innerHTML = "";
});
