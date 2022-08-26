$(document).ready(function(){
  var imageBoard = new DrawingBoard.Board('div', {
    background: "#fff",
    color: "#ff0",
    size: 30,
    controls: [
      'Color',
      { Size: { type: "range" } },
      { Navigation: { back: true, forward: true } },
      'DrawingMode'
    ],
    webStorage: 'local'
});
  $("#button").click(function(){
    domtoimage.toBlob(document.getElementById('div'))
  .then(function (blob) {
      window.saveAs(blob, 'photo.png');
  });
  })
})
