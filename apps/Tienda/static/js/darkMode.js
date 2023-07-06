const preferedColorScheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
const slider = document.getElementById('slider');

const setTheme = (theme) => {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
}

slider.addEventListener('click', ()  => {
    let switchToTheme = localStorage.getItem('theme') === 'dark' ? 'light' : 'dark';
    setTheme(switchToTheme);
});

setTheme(localStorage.getItem('theme') || preferedColorScheme);

// --------------------------------------------------------------------

const toggle= document.getElementById('toggleDark');
const body = document.querySelector('body');

toggle.addEventListener('click', function () {
    this.classList.toggle('fa-moon');
    if (this.classList.toggle(' sun ')) {
        body.style.background = 'white';
        body.style.color = 'black' ;
        body.style.transition = '2s ';
    } 
    else{
        body.style.background = 'black';
        body.style.color = 'white' ;
        body.style.transition = '2s ';
    }
});
