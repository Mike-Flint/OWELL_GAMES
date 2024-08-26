from django.shortcuts import render

from API import languageAllSites
from django.utils import translation

# Create your views here.
def BS(request):
    print(translation.get_language())
    return render(request,"BS/MainBS.html", languageAllSites.listBS["en"])

def BS_languageSite(request,lang):
    global list
    if lang.lower() in ["fv", "en", "cn", "es", "ua", "in", "kr", "pl", "tr", "de", "br", "jp", "it"]:
        return render(request,"BS/MainBS.html", languageAllSites.listBS[lang.lower()])

    else:
        return render(request,"BS/MainBS.html", languageAllSites.listBS["en"])



