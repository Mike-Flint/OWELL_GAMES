function onEntry(entries, observer) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
        entry.target.classList.add('AnimOriginal');
        }
    });
    }

function setupAnimations() {
    const options = { 
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(onEntry, options);
    const animatedElements = document.querySelectorAll('.AnimLeft, .AnimRight , .AnimTop');

    animatedElements.forEach(el => {
        observer.observe(el);
    });
}

window.addEventListener('load', setupAnimations);



let openORclose = false;
function menu_language(){
    let menu = document.getElementById("menu");
    let arrow = document.getElementById("arrow");
    let btn_language = document.getElementById("btn_language")
    if (menu){
        if (openORclose) {
            menu.style.display = "none";
            arrow.style.transform = "rotate(0deg)";
            btn_language.style.paddingBottom = "7px";
            btn_language.style.paddingTop = "7px";
            openORclose = false;

        }
        else{
            menu.style.display = "block";
            arrow.style.transform = "rotate(-180deg)";
            if (window.innerWidth > 1220) {
                btn_language.style.paddingTop = "25px";
            }
            else{
                btn_language.style.paddingTop = "20px";
            }
            btn_language.style.paddingBottom = "100px";
            openORclose = true;
        }
    }
}