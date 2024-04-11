window.onscroll = function() {myFunction()};

function myFunction() {
  if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
    document.getElementById("navbar").style.backgroundColor= "black";
  } else {
    document.getElementById("navbar").style.backgroundColor = "transparent";
  }
}

document.addEventListener("DOMContentLoaded", (event) => {
  if(window.location.href=="http://localhost:8000/about/")
    document.getElementById("content").innerHTML="EXPERIENCE THE ESSENCE OF BEAUTY WITH SKIN-SAVIOUR";
  else if(window.location.href=="http://localhost:8000/quiz/")
    document.getElementById("content").innerHTML="Take Our Skin Quiz To Receive Expert Insights";
  else if(window.location.href=="http://localhost:8000/skin_treatment/")
    document.getElementById("content").innerHTML="SKIN TREATMENT";
  else if(window.location.href=="http://localhost:8000/tips/")
    document.getElementById("content").innerHTML="TIPS";
  else if(window.location.href=="http://localhost:8000/contact_us/")
    document.getElementById("content").innerHTML="Stay Connected With Us For More SkinCare Insights";
  else if(window.location.href=="http://localhost:8000/register/")
    document.getElementById("content").innerHTML="Register/SignIn";

    document.addEventListener("click",()=>{
      var element=document.getElementById("dropdown");
      element.style.display="none";
    })
});


// profile dropdown

var dropdown=document.getElementById("profile");
dropdown.addEventListener("click",(event)=>{
  event.stopPropagation()
  var element=document.getElementById("dropdown");
  if(element.style.display=="block"){
    element.style.display="none";
  }
  else{
    element.style.display="block";
  }
  
})
  


function logout(event){
  var overlay = document.getElementById('overlay');
    var popup = document.getElementById('popup');
    var child=document.createElement("p");
    var timer=document.createElement("div");


    child.classList.add("loginerror");
    timer.classList.add("timer-bar")
    child.innerText="successful loggedout";
    popup.appendChild(child);
    child.appendChild(timer);
    overlay.style.display = 'block';


    var width=100;
    timerInterval= setInterval(function () {
    width = width-3;
    timer.style.width = width + '%';
    }, 100);


    setTimeout(()=>{
        overlay.style.display = 'none';
        clearInterval(timerInterval);
    }, 3000)
}