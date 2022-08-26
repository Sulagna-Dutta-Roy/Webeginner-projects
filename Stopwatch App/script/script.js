let Interval;
let btnStart = document.getElementById('btn-start');
let btnStop = document.getElementById('btn-stop');
let btnReset = document.getElementById('btn-reset');
let btnFlag = document.getElementById('btn-flag');
let hours = 0, minutes = 0, seconds = 0, mils = 0;
let outputHours = document.getElementById('hours');
let outputMinutes = document.getElementById('minutes');
let outputSeconds = document.getElementById('seconds');
let outputMils = document.getElementById('mils');
let flagsArray = [];

btnStart.addEventListener('click', () => {
    clearInterval(Interval);
    Interval = setInterval(startTime, 10);
});

btnStop.addEventListener('click', () => {
    clearInterval(Interval);
});

btnReset.addEventListener('click', () => {
    clearInterval(Interval);
    hours = '00';
    minutes = '00';
    seconds = '00';
    mils = '00';
    outputHours.innerHTML = hours;
    outputMinutes.innerHTML = minutes;
    outputSeconds.innerHTML = seconds;
    outputMils.innerHTML = mils;
    flagsArray = [];
    localStorage.clear();
    update();
});

btnFlag.addEventListener('click', () => {
    let myFlag = document.getElementById('curTime').innerText;
    if (localStorage.getItem('flags') == null) {
        flagsArray.push(myFlag);
        localStorage.setItem('flags', JSON.stringify(flagsArray));
    }
    else {
        flagsArrayStr = localStorage.getItem('flags');
        flagsArray = JSON.parse(flagsArrayStr);
        flagsArray.push(myFlag);
        localStorage.setItem('flags', JSON.stringify(flagsArray));
    }
    update();
});

function update() {
    let s = "";
    flagsArray.forEach((element, index) => {
        s += `<tr>
                <th scope="row">${index}</th>
                <td>${element}</td>
                <td><button class="btn btn-danger" onclick="deleteFlag(${index})">Delete</button></td>
                </tr>`;
    });
    document.getElementById('tableBody').innerHTML = s;
}

function deleteFlag(index) {
    flagsArray.splice(index, 1);
    localStorage.setItem('flags', JSON.stringify(flagsArray));
    update();
}

window.onload = ()=>{
    flagsArray = [];
    localStorage.clear();
    update();
}

function startTime() {
    // Milli Seconds Part
    mils++;
    if (mils < 10)
        outputMils.innerHTML = '0' + mils;
    else {
        if (mils < 99)
            outputMils.innerHTML = mils;
        else {
            // Seconds Part
            seconds++;
            outputMils.innerHTML = '00';
            mils = 0;
            if (seconds < 10)
                outputSeconds.innerHTML = '0' + seconds;
            else {
                if (seconds < 60)
                    outputSeconds.innerHTML = seconds;
                else {
                    // Minutes Part
                    minutes++;
                    seconds = 0;
                    outputSeconds.innerHTML = '00';
                    if (minutes < 10)
                        outputMinutes.innerHTML = '0' + minutes;
                    else {
                        if (minutes < 60)
                            outputMinutes.innerHTML = minutes;
                        else {
                            // Hours Part
                            hours++;
                            minutes = 0;
                            outputMinutes.innerHTML = '00';
                            if (hours < 10)
                                outputHours.innerHTML = '0' + hours;
                            else {
                                outputHours.innerHTML = hours;
                            }
                        }
                    }
                }
            }
        }
    }
}