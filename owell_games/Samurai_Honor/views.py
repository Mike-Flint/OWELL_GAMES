from django.shortcuts import render

from API import languageAllSites


def SH(request):
    return render(request,"SH/MainSH.html", languageAllSites.listSH["en"])

def SH_languageSite(request,lang):
    global list
    if lang.lower() in ["en","ua"]:
        return render(request,"SH/MainSH.html", languageAllSites.listSH[lang.lower()])

    else:
        return render(request,"SH/MainSH.html", languageAllSites.listSH["en"])

