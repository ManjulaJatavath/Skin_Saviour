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
    document.getElementById("content").innerHTML="QUIZ";
  else if(window.location.href=="http://localhost:8000/skin_treatment/")
    document.getElementById("content").innerHTML="SKIN TREATMENT";
  else if(window.location.href=="http://localhost:8000/tips/")
    document.getElementById("content").innerHTML="TIPS";
  else if(window.location.href=="http://localhost:8000/contact_us/")
    document.getElementById("content").innerHTML="CONTACT US";
});