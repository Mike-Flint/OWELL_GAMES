function onEntry(entries, observer) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
        entry.target.classList.add('AnimOriginal');
        }
    });
}

window.addEventListener('load', setupAnimations);
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

async function applyLanguage(lang,site) {
    if (!languagesData[lang]) {
        const requestUrl = `${window.location.origin}/api/v1/${site}/languages/${lang}`;
        const response = await fetch(requestUrl);
        if (!response.ok) {
            throw new Error('Відповідь мережі була не в порядку');
        }
        const data = await response.json();
        languagesData[lang] = data;
    }
    const data = languagesData[lang];
    for (let key in data) {
        let elems = document.querySelectorAll('.lng-' + key);
        elems.forEach(elem => {
            if (elem) {
                elem.innerHTML = data[key];
            }
        });
    }
}

function updateLinks(lang) {
    document.querySelectorAll('a.BS_link').forEach(link => {
        link.href = `${window.location.origin}/BoxStorm/${lang.toLowerCase()}`;
    });
    document.querySelectorAll('a.SH_link').forEach(link => {
        link.href = `${window.location.origin}/SamuraiHonor/${lang.toLowerCase()}`;
    });
    document.querySelectorAll('a.Main_link').forEach(link => {
        link.href = `${window.location.origin}/${lang.toLowerCase()}`;
    });
}

function GlobalScrol(num){
    if (window.innerWidth >= 1220) {
        window.scrollTo({
            top: window.scrollY + num,
            behavior: 'smooth' 
        });
    }
    else {
        window.scrollTo({
            top: window.scrollY + 500,
            behavior: 'smooth'
        });
    }
}
function URL_Check(way){
    if ( window.location.origin + way == window.location.href) {
        history.replaceState(null, '',  window.location.origin + way + "en");
    }
    else {
        if (!["fv", "en", "cn", "es", "ua", "in", "kr", "pl", "tr", "de", "br", "jp", "it"].includes(window.location.pathname.replace(/\/$/, '').slice(-2).toLowerCase())){
            history.replaceState(null, '',  window.location.origin + way +"en");
        }
    }
}

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