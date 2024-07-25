from django.shortcuts import render

from API import languageAllSites

# Create your views here.
def main(request):
    return render(request,"main/main.html", languageAllSites.listMain["en"])

def languageSite(request,lang):
    global list
    if lang.lower() in ["en","ua"]:
        return render(request,"main/main.html", languageAllSites.listMain[lang.lower()])

    else:
        return render(request,"main/main.html", languageAllSites.listMain["en"])
