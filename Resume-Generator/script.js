function addNewExp() {
    let newnode = document.createElement("textarea");
    newnode.classList.add("form-control");
    newnode.style.marginTop = "20px";
    newnode.classList.add("wefield");
    newnode.setAttribute("rows", 3);
    newnode.setAttribute("placeholder", "Enter your Work Experience");
  
    let weAdd = document.getElementById("we");
    let weAddButton = document.getElementById("weAddButton");
  
    weAdd.insertBefore(newnode, weAddButton);
  }
  
  function addNewEdu() {
    let newnode = document.createElement("textarea");
    newnode.classList.add("form-control");
    newnode.style.marginTop = "20px";
    newnode.classList.add("edufield");
    newnode.setAttribute("rows", 3);
    newnode.setAttribute("placeholder", "Enter your Education");
  
    let weAdd = document.getElementById("edu");
    let weAddButton = document.getElementById("EAddButton");
  
    weAdd.insertBefore(newnode, weAddButton);
  }
  
  //generating cv
  
  function generateResume() {
    let file = document.getElementById("imgField").files[0];
    console.log(file);
  
    let reader = new FileReader();
  
    reader.readAsDataURL(file);
  
    //set image
  
    reader.onloadend = function () {
      document.getElementById("my-img").src = reader.result;
    };
  
    let nameField = document.getElementById("namefield").value;
  
    document.getElementById("nameT1").innerHTML = nameField;
    // document.getElementById("nameT2").innerHTML = nameField;
  
    let contactNo = document.getElementById("contactfield").value;
    document.getElementById("noT").innerHTML = contactNo;
  
    let email = document.getElementById("emailfield").value;
    document.getElementById("emailT").innerHTML = email;
  
    let address = document.getElementById("addressfield").value;
    document.getElementById("addressT").innerHTML = address;
  
    let Github = document.getElementById("githubfield").value;
    document.getElementById("githubT").innerHTML = Github;
  
    let Linkedin = document.getElementById("linkedinfield").value;
    document.getElementById("linkedinT").innerHTML = Linkedin;
  
    let Twitter = document.getElementById("twitterfield").value;
    document.getElementById("twitterT").innerHTML = Twitter;
  
    let Website = document.getElementById("websitefield").value;
    document.getElementById("websiteT").innerHTML = Website;
  
    let Skill = document.getElementById("skillfield").value;
    document.getElementById("skillT").innerHTML = Skill;
  
    let obj = document.getElementById("objfield").value;
    document.getElementById("objT").innerHTML = obj;
  
    // experience
    let work = document.getElementsByClassName("wefield");
  
    let str = "";
    for (let e of work) {
      str = str + `<li> ${e.value}</li>`;
    }
    document.getElementById("weT").innerHTML = str;
  
    //education
    let Education = document.getElementsByClassName("edufield");
  
    let str2 = "";
    for (let e of Education) {
      str2 = str2 + `<li> ${e.value}</li>`;
      console.log(str2);
    }
    document.getElementById("eduT").innerHTML = str2;
  
    document.getElementById("cv-form").style.display = "none";
  
    document.getElementById("cv-template").style.display = "block";
  }
  
  //printing
  
  function printResume() {
    console.log("clicked");
    window.print();
  }
  