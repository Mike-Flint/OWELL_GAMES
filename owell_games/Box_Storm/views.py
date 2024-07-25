from django.shortcuts import render

from API import languageAllSites

# Create your views here.
def BS(request):
    return render(request,"BS/MainBS.html", languageAllSites.listBS["en"])

def BS_languageSite(request,lang):
    global list
    if lang.lower() in ["en","ua"]:
        return render(request,"BS/MainBS.html", languageAllSites.listBS[lang.lower()])

    else:
        return render(request,"BS/MainBS.html", languageAllSites.listBS["en"])



