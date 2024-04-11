var error_section=document.querySelector(".errorlist")?document.querySelector(".errorlist"):""
if(error_section){
    var error=error_section.querySelector("li");

    var overlay = document.getElementById('overlay');
    var child=document.createElement("p");
    var timer=document.createElement("div");


    child.classList.add("loginerror");
    timer.classList.add("timer-bar")
    child.innerText=error.innerText;
    popup.appendChild(child);
    child.appendChild(timer);
    overlay.style.display = 'block';


    var width=100;
    timerInterval= setInterval(function () {
    width = width-2;
    timer.style.width = width + '%';
    }, 100);


    setTimeout(()=>{
        popup.style.display="none";
        overlay.style.display = 'none';
        clearInterval(timerInterval);
    }, 5000)
}