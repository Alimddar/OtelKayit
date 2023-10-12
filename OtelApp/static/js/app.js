const darkModeToggle = document.getElementById("darkModeToggle");

if(darkModeToggle){
    darkModeToggle.addEventListener('click', function(){
        if(document.body.getAttribute('data-bs-theme') == 'dark'){
            document.body.setAttribute('data-bs-theme','light');
            localStorage.setItem('theme', 'light');
        }else {
            document.body.setAttribute('data-bs-theme','dark');
            localStorage.setItem('theme', 'dark');
        }
    })
}

if(localStorage.getItem('theme') == 'dark'){
    document.body.setAttribute('data-bs-theme' ,'dark')
}else {
    document.body.setAttribute('data-bs-theme',"light")
}

