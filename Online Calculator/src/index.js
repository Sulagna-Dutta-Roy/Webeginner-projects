
//Here is script...
//Hope You like it..

$(document).ready(function(){
  $('#one').click(function(){
    document.forms.display.value += 1;
  });
  $('#two').click(function(){
    document.forms.display.value += 2;
  });
  $('#three').click(function(){
    document.forms.display.value += 3;
  });
  $('#four').click(function(){
    document.forms.display.value += 4;
  });
  $('#five').click(function(){
    document.forms.display.value += 5;
  });
  $('#six').click(function(){
    document.forms.display.value += 6;
  });
  $('#seven').click(function(){
    document.forms.display.value += 7;
  });
  $('#eight').click(function(){
    document.forms.display.value += 8;
  });
  $('#nine').click(function(){
    document.forms.display.value += 9;
  });
  $('#zero').click(function(){
    document.forms.display.value += 0;
  });
  $('#add').click(function(){
    document.forms.display.value += '+';
  });
  $('#subs').click(function(){
    document.forms.display.value += '-';
  });
  $('#multi').click(function(){
    document.forms.display.value += '*';
  });
  $('#divide').click(function(){
    document.forms.display.value += '/';
  });
  $('#dot').click(function(){
    document.forms.display.value += '.';
  });
  $('#equal').click(function(){
    if (display.value == "") {
      alert("Please enter any numbers to calculate!");
    }else{
      document.forms.display.value =
      eval(document.forms.display.value);
    }
  });
  $('#clear').click(function(){
    document.forms.display.value = "";
  });
})

