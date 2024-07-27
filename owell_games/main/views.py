from django.shortcuts import render

from API import languageAllSites

# Create your views here.
def main(request):
    return render(request,"main/main.html", languageAllSites.listMain["en"])

def languageSite(request,lang):
    global list
    if lang.lower() in ["fv", "en", "cn", "es", "ua", "in", "kr", "pl", "tr", "de", "br", "jp", "it"]:
        return render(request,"main/main.html", languageAllSites.listMain[lang.lower()])

    else:
        return render(request,"main/main.html", languageAllSites.listMain["en"])
