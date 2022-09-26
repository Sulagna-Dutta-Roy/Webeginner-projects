var date = new Date();
var day = date.getDate();
var month = date.getMonth()+1;
var year = date.getFullYear();
if(day<=9){
  day = "0"+day;
}
if(month<=9){
  month = "0"+month;
}
document.getElementById("currDate").innerHTML = `Today's Date is ${day}/${month}/${year} `;

function age() {
    var d1 = document.getElementById('date').value;
    var m1 = document.getElementById('month').value;
    var y1 = document.getElementById('year').value;


    var date = new Date();
    var d2 = date.getDate();
    var m2 = 1 + date.getMonth();
    var y2 = date.getFullYear();
    var month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    if(d1 > d2){
      d2 = d2 + month[m2 - 1];
      m2 = m2 - 1;
    }
    if(m1 > m2){
      m2 = m2 + 12;
      y2 = y2 - 1;
    }
    var d = d2 - d1;
    var m = m2 - m1;
    var y = y2 - y1;

    document.getElementById('age').innerHTML = 'You are '+y+' Years '+m+' Months '+d+' Days Old';
    if(isNaN(d1) || isNaN(m1) || isNaN(y1) || d1<=0 || m1<=0||y1<=0){
      document.getElementById('age').innerHTML = 'Invalid Date or Empty';
    }
    else{
      if(m1>12 || d1>month[m1-1]){
        document.getElementById('age').innerHTML = "Invalid DOB Entered";
      }


      if(y1>=y2){
        if(y1>y2){
          document.getElementById('age').innerHTML = "Future DOB is not Allowed";
        }
        else{
          if(m1>=m2){
            if(m1>m2){
              document.getElementById('age').innerHTML = "Future DOB is not Allowed";
            }
            else{
              if(d1>d2){
                document.getElementById('age').innerHTML = "Future DOB is not Allowed";
              }
            }
          }
        }

      }
    }
  }
