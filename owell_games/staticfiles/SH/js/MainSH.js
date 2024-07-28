
//scroll was busy :(
function scrolll(){
    if (window.innerWidth >= 1220) {
        window.scrollTo({
            top: window.scrollY + 800,
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

if ( window.location.origin + "/SamuraiHonor/" == window.location.href) {
    history.replaceState(null, '',  window.location.origin + "/SamuraiHonor/en");
}
else {
    if (!["fv", "en", "cn", "es", "ua", "in", "kr", "pl", "tr", "de", "br", "jp", "it"].includes(window.location.pathname.replace(/\/$/, '').slice(-2).toLowerCase())){
        history.replaceState(null, '',  window.location.origin + "/SamuraiHonor/en");
    }
}

async function language(lang){
    history.replaceState(null, '',  window.location.origin + "/SamuraiHonor/" + lang);
    const requestUrl = window.location.origin +`/api/v1/SH/languages/${lang}`;
    const response = await fetch(requestUrl);
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const data = await response.json();

    document.querySelectorAll('a.BS_link').forEach(link => {
        link.href = window.location.origin + '/BoxStorm/' + data["lng"].toLowerCase();
    });
    document.querySelectorAll('a.SH_link').forEach(link => {
        link.href = window.location.origin + '/SamuraiHonor/' + data["lng"].toLowerCase();
    });
    document.querySelectorAll('a.Main_link').forEach(link => {
        link.href = window.location.origin + '/' + data["lng"].toLowerCase();
    });

    for (let key in data) {
        let elems = document.querySelectorAll('.lng-' + key);
        elems.forEach(elem => {
            if(elem) {
                elem.innerHTML = data[key];
            }
        });
    }
}
