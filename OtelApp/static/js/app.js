const darkModeToggle = document.getElementById("darkModeToggle");


darkModeToggle.addEventListener('click', function(){
    if(document.body.getAttribute('data-bs-theme') == 'dark'){
        document.body.setAttribute('data-bs-theme','light');
        localStorage.setItem('theme', 'light');
    }else {
        document.body.setAttribute('data-bs-theme','dark');
        localStorage.setItem('theme', 'dark');
        
    }
})

if(localStorage.getItem('theme') == 'dark'){
    document.body.setAttribute('data-bs-theme' ,'dark')
    darkModeToggle.innerHTML = `<i class="fa-solid fa-moon"></i> / <i class="fa-solid fa-sun"></i>`
}else {
    document.body.setAttribute('data-bs-theme',"light")
    darkModeToggle.innerHTML = `<i class="fa-solid fa-moon"></i> / <i class="fa-solid fa-sun"></i>`
}