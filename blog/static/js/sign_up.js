var label = document.getElementsByTagName("label");
var input = document.getElementsByTagName("input");
var username = document.getElementById("id_username");
var pw1 = document.getElementById("id_password1");
var pw2 = document.getElementById("id_password2");
var helptext = document.getElementsByClassName("helptext");
for(var i=0; i<3; i++){
    helptext[i].innerText = "";
    label[i].innerText = "";
    input[i].setAttribute("class", "form-control");
}
pw2.setAttribute("class", "form-control");
username.setAttribute("placeholder", "Username");
pw1.setAttribute("placeholder", "Password");
pw2.setAttribute("placeholder", "Password confirmation");