
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
    if (!["fv", "en", "cn", "es", "ua", "in", "kr", "pl", "tr", "de", "br", "jp", "it"].includes(window.location.pathname.substr(1).toLowerCase())){
        history.replaceState(null, '',  window.location.origin + "/SamuraiHonor/en");
    }
}

async function language(lang){
    history.replaceState(null, '',  window.location.origin + "/SamuraiHonor/" + lang);
    const requestUrl = `http://127.0.0.1:8000/api/v1/BS/languages/${lang}`;
    const data = await JsonRequestUrl(requestUrl);

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
        let elem = document.querySelector('.lng-' + key);
        if (elem) {
            elem.innerHTML = data[key];
        }
    }
}

async function JsonRequestUrl(requestUrl) {
    try {
      const response = await fetch(requestUrl);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('There was a problem with the fetch operation:', error);
    }
  }
