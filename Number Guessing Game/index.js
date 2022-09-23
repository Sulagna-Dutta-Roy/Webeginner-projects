var ans = document.getElementById("output");
var t=0;
var tr=document.getElementById("tries");
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
<<<<<<< HEAD
        ans.style.color= "#00FFAB";
=======
        ans.style.color= "#006400";
        t++;
>>>>>>> 92d675b532b475346458fb0184de69a890533cac
    }
    else if(random>guess && random>1)
    {
        ans.innerHTML="Your Guess is too Low";
        ans.style.color="red";
        t++;       
    }
    else if(random<guess && guess<100)
    {
        ans.innerHTML="Your Guess is too high";
        ans.style.color="red"; 
        t++;      
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
    tr.innerHTML=t;
    }