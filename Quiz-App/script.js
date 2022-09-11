const quizData = [
    {
      question: " Q1. The default link color for hyperlinks? ",
      a: "green",
      b: "yellow",
      c: "blue",
      d: "red",
      ans: "ans-3",
    },
    {
      question: " Q2. What is the full form of HTML ",
      a: "Hypertext Markup Language",
      b: "Hypermedia Markup Language",
      c: "Hyper makrup language",
      d: "none of above",
      ans: "ans-1",
    },
  
    {
      question: "Q3. What is the full form of JS",
      a: "JavaScript",
      b: "Java speech",
      c: "Java language",
      d: "none of above",
      ans: "ans-1",
    },
  
    {
      question: "Q4. What is the full form of CSS",
      a: "Cascading Speed Sheet",
      b: "Cascading Style Sheet",
      c: "Colourful style sheet",
      d: "none of above",
      ans: "ans-2",
    },
  
    {
      question: "Q5. Which tag is used to underline text",
      a: "<a>",
      b: "<hr>",
      c: "<br>",
      d: "<u>",
      ans: "ans-4",
    },
  
    {
      question: "Q6. To make a comment in HTML you use ",
      a: "<!-- -->",
      b: "//",
      c: "/* ",
      d: "#",
      ans: "ans-1",
    },
  
    {
      question: "Q7. CSS to make text of all <p> tags red",
      a: "p{colour:red}",
      b: "p-style{color:red}",
      c: "p{color:red}",
      d: "p{color style :red}",
      ans: "ans-3",
    },
  
    {
      question: "Q8. JavaScript files have the file extention ",
      a: ".java",
      b: ".css",
      c: ".html",
      d: ".js",
      ans: "ans-4",
    },
  
    {
      question: "Q9. Choose the correct HTML element for largest heading",
      a: "<h1>",
      b: "<head>",
      c: "<h6>",
      d: "<heading>",
      ans: "ans-1",
    },
  
    {
      question:
        "Q10. What is the correct HTML element for inserting a line break ",
      a: "<break>",
      b: "<hr>",
      c: "<lb>",
      d: "<br>",
      ans: "ans-4",
    },
  ];
  
  const question = document.querySelector(".question");
  const option1 = document.querySelector("#option-1");
  const option2 = document.querySelector("#option-2");
  const option3 = document.querySelector("#option-3");
  const option4 = document.querySelector("#option-4");
  const submit = document.querySelector("#submit");
  const answers = document.querySelectorAll(".answer");
  const showScore=document.querySelector("#showScore");
  
  let questionCount = 0;
  
  let score = 0;
  
  const loadQuestion = () => {
    const questionList = quizData[questionCount];
  
    question.innerText = questionList.question;
    option1.innerText = questionList.a;
    option2.innerText = questionList.b;
    option3.innerText = questionList.c;
    option4.innerText = questionList.d;
  
    
  };
  loadQuestion();
  
  function getanswer() {
    let answer;
    answers.forEach((currAns) => {
      if (currAns.checked) {
        answer = currAns.id;
      }
    });
    return answer;
  }
   const deselectAll=()=>{
      answers.forEach((curAnsElem)=> curAnsElem.checked=false);
   }
  
  submit.addEventListener("click", () => {
    const checkedAnswer = getanswer();
    console.log(checkedAnswer);
  
    if (checkedAnswer === quizData[questionCount].ans) {
      score++;  
    } 
  
    deselectAll();
    questionCount++;
    if (questionCount < quizData.length) {
      loadQuestion();
      
    }
    else{
      
      showScore.innerHTML=`<h1> You scored ${score}/${quizData.length}👍 </h1>
      <button class="btn" onClick="location.reload()">Try Again</button>`;
      showScore.classList.remove('scoreArea'); 
      submit.style.display='none'; 
  }
  
    
  });
  