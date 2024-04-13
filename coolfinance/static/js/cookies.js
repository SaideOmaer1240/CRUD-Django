var mgCookies = document.getElementById('mesageCookie')

function aceito(){
    localStorage.aceita = 'sim'
    mgCookies.classList.remove('mostrar')
}

if(localStorage.aceita == 'sim'){
    mgCookies.classList.remove('mostrar')
}else{
    mgCookies.classList.add('mostrar')
}