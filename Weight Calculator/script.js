function convertWeight(){
    let val = document.getElementById("input_value");
    let result = document.getElementById("result");
    let input = document.getElementById("inputType");
    let output = document.getElementById("resultType");
    val.addEventListener("keyup", convertWeight);
    inputType.addEventListener("change", convertWeight);
    resultType.addEventListener("change", convertWeight);

    let inputValue = input.value;
    let outputValue = output.value;
    if(inputValue === "Pounds" && outputValue === "Kilograms"){
        result.value = Number(val.value) * 0.45359237 ;
      }else if(inputValue === "Pounds" && outputValue === "Ounces"){
        result.value = Number(val.value) *16;
      }else if(inputValue === "Pounds" && outputValue === "Stones"){
        result.value = (val.value)/14;
      }
      if(inputValue === "Kilograms" && outputValue === "Pounds"){
        result.value = Number(val.value)*2.20462;
      }else if(inputValue === "Kilograms" && outputValue === "Ounces"){
        result.value = Number(val.value) *35.274 ;
      }else if(inputValue === "Kilograms" && outputValue === "Stones"){
        result.value = (val.value)/6.35;
      }
      if(inputValue === "Ounces" && outputValue === "Pounds"){
        result.value = Number(val.value)/16;
      }else if(inputValue === "Ounces" && outputValue === "Kilograms"){
        result.value = Number(val.value)/35.3;
      }else if(inputValue === "Ounces" && outputValue === "Stones"){
        result.value = Number(val.value)/224;
      }
      if(inputValue === "Stones" && outputValue === "Pounds"){
        result.value = Number(val.value)*14;
      }else if(inputValue === "Stones" && outputValue === "Kilograms"){
        result.value = Number(val.value ) *6.35029 ;
      }else if(inputValue === "Stones" && outputValue === "Ounces"){
        result.value = (val.value)*224;
      }

    }

    function reset(){
      convertWeight();
    }