//scroll was busy :(
function scrolll(){
    GlobalScrol(800);
}
URL_Check("/BoxStorm/");
languagesData = {};
async function language(lang){
    history.replaceState(null, '',  window.location.origin + "/BoxStorm/" + lang);
    applyLanguage(lang, "BS");
    updateLinks(lang);
}
    
