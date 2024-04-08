window.onscroll = function() {myFunction()};

function myFunction() {
  if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
    document.getElementById("navbar").style.backgroundColor= "black";
  } else {
    document.getElementById("navbar").style.backgroundColor = "transparent";
  }
}

document.addEventListener("DOMContentLoaded", (event) => {
  if(window.location.href=="http://127.0.0.1:8000/about/")
    document.getElementById("content").innerHTML="EXPERIENCE THE ESSENCE OF BEAUTY WITH SKIN-SAVIOUR";
  else if(window.location.href=="http://127.0.0.1:8000/quiz/")
    document.getElementById("content").innerHTML="Take Our Skin Quiz To Receive Expert Insights";
  else if(window.location.href=="http://127.0.0.1:8000/skin_treatment/")
    document.getElementById("content").innerHTML="SKIN TREATMENT";
  else if(window.location.href=="http://127.0.0.1:8000/tips/")
    document.getElementById("content").innerHTML="TIPS";
  else if(window.location.href=="http://127.0.0.1:8000/contact_us/")
    document.getElementById("content").innerHTML="Stay Connected With Us For More SkinCare Insights";
  else if(window.location.href=="http://127.0.0.1:8000/register/")
    document.getElementById("content").innerHTML="Register/SignIn";
});