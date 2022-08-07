let  uppercase = document.getElementById("uppercase");
let lowercase = document.getElementById("lowercase");
let bold = document.getElementById("bold");
let italic = document.getElementById("italic");
let underline = document.getElementById("underline");



let input_text = document.getElementById("input_text");

// switch between the classes of the buttons to change the style of the button
function uppercase_function() {
    if (uppercase.classList.contains("active")) {

        uppercase.classList.remove("active");
        input_text.style.textTransform = "normal";
    }
    else {

        uppercase.classList.add("active");
        input_text.style.textTransform = "uppercase";
    }
}
function lowercase_function() {
    if (lowercase.classList.contains("active")) {

        lowercase.classList.remove("active");
        input_text.style.textTransform = "normal";
    }
    else {


        lowercase.classList.add("active");
        input_text.style.textTransform = "lowercase";
    }
}
function bold_function() {
    if (bold.classList.contains("active")) {

        bold.classList.remove("active");
        input_text.style.fontWeight = "normal";
    }
    else {


        bold.classList.add("active");
        input_text.style.fontWeight = "bold";
    }
}
function italic_function() {
    if (italic.classList.contains("active")) {

        italic.classList.remove("active");
        input_text.style.fontStyle = "normal";
    }
    else {


        italic.classList.add("active");
        input_text.style.fontStyle = "italic";``
    }
}
function underline_function() {
    if (underline.classList.contains("active")) {

        underline.classList.remove("active");
        input_text.style.textDecoration = "none";
    }
    else {


        underline.classList.add("active");
        input_text.style.textDecoration = "underline";
    }
}




// events for the buttons

uppercase.addEventListener("click", uppercase_function);
lowercase.addEventListener("click", lowercase_function);
bold.addEventListener("click", bold_function);
italic.addEventListener("click", italic_function);
underline.addEventListener("click", underline_function);
