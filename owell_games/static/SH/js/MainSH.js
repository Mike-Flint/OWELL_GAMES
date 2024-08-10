//scroll was busy :(
function scrolll(){
    GlobalScrol(800);
}
URL_Check("/SamuraiHonor/");
languagesData = {};
async function language(lang){
    history.replaceState(null, '',  window.location.origin + "/SamuraiHonor/" + lang);
    applyLanguage(lang, "SH");
    updateLinks(lang);
}
