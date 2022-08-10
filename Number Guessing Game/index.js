var ans = document.getElementById("output");

var enter = document.getElementById("enter");
var again = document.getElementById("again");
var random = Math.floor(Math.random()*100)+1;
enter.addEventListener('click',check);
again.addEventListener('click',function(){
    location.reload();
})
document.addEventListener('keypress',function(e){
        if(e.key=="Enter")
        check();
        
        
})
function check(){
    var guess = document.getElementById("user").value;
    if(random == guess)
    {
        ans.innerHTML ="Your Guess is Correct "+random+" is the number";
        ans.style.color= "#006400";
    }
    else if(random>guess && random>1)
    {
        ans.innerHTML="Your Guess is too Low";
        ans.style.color="red";       
    }
    else if(random<guess && guess<100)
    {
        ans.innerHTML="Your Guess is too high";
        ans.style.color="red";       
    }
    else if(guess<1 || guess>100)
    {
        ans.innerHTML="Out of Range";
        ans.style.color="red";       
    }
    else{
        ans.innerHTML="Enter Numbers only";
        ans.style.color="red";       
    }
    }
    
    

