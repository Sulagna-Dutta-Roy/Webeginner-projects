let colorOne = document.getElementById("color_one");
let colorTwo = document.getElementById("color_two");
let currentdir = "to top";
let outputcode = document.getElementById("code");

// @dev function setdirection() helps to set the direction of the gradient
function setdirection(value, _this) {
  let direction = document.querySelectorAll(".buttons button");
  direction.forEach((e) => {
    e.classList.remove("active");
  });
  _this.classList.add("active");
  currentdir = value;
}

// @dev function generate() creates the gradient code and displays it in the output code section
function generate() {
  outputcode.value = `background-image: linear-gradient(${currentdir}, ${colorOne.value}, ${colorTwo.value});`;
  document.getElementById(
    "body"
  ).style.backgroundImage = `linear-gradient(${currentdir}, ${colorOne.value}, ${colorTwo.value})`;
}

// @dev function copy() copies the code to the clipboard
function copy() {
  /* Get the text field */
  var copyText = document.getElementById("code");

  /* Select the text field */
  copyText.select();
  copyText.setSelectionRange(0, 99999); /* For mobile devices */

  /* Copy the text inside the text field */
  navigator.clipboard.writeText(copyText.value);

  /* Alert the copied text */
  alert("Copied the text: " + copyText.value);
}
