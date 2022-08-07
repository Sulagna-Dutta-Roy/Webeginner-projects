// Fuction to generate a random rgb color

function changeColor() {
    const r = parseInt(Math.random() * 256);
    const g = parseInt(Math.random() * 256);
    const b = parseInt(Math.random() * 256);
    const a = Math.random();

    const color = "rgba(" + r + "," + g + "," + b + "," + a + ")";
    document.body.style.background = color;

}