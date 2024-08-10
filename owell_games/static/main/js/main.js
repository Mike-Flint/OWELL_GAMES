//scroll was busy :(
function scrolll(){
    GlobalScrol(1000);
}
URL_Check("/");
languagesData = {};
async function language(lang){
    history.replaceState(null, '',  window.location.origin + "/" + lang);
    applyLanguage(lang, "main");
    updateLinks(lang);
}