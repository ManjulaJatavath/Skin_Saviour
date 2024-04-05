window.onscroll = function() {myFunction()};

function myFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 10) {
    document.getElementById("navbar").style.backgroundColor= "black";
  } else {
    document.getElementById("navbar").style.backgroundColor = "transparent";
  }
}