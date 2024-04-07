let register_var=document.getElementById("register");
let signin_var=document.getElementById("signin");
    
function register(){
    register_var.style.display="";
    signin_var.style.display="none";
}

function signin(){
    register_var.style.display="none";
    signin_var.style.display="flex";
}