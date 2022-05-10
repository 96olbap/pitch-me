var btnLogin = document.getElementsByClassName('btn-default');
var idLogin = document.getElementById('login');
btnLogin.onclick = function() {
    idLogin.innerHTML = '<p>We\'re happy to see you again, </p>';
}