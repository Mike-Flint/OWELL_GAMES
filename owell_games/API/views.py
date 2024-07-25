
from rest_framework.views import APIView
from rest_framework.response import Response

from . import languageAllSites


class MainAPILanguage(APIView):
    def get(self, request, lang):
        #["en","ua","fv","cn","es","in","kr","pl","tr","de","br","jp","it"]
        if lang.lower() in ["en","ua"]:
            print(lang)
            return Response(languageAllSites.listMain[lang.lower()])
            
        return Response(list["en"])
    
      
class BS_MainAPILanguage(APIView):
    def get(self, request, lang):
        #["en","ua","fv","cn","es","in","kr","pl","tr","de","br","jp","it"]
        if lang.lower() in ["en","ua"]:
            print(lang)
            return Response(languageAllSites.listBS[lang.lower()])
            
        return Response(list["en"])


class SH_MainAPILanguage(APIView):
    def get(self, request, lang):
        #["en","ua","fv","cn","es","in","kr","pl","tr","de","br","jp","it"]
        if lang.lower() in ["en","ua"]:
            print(lang)
            return Response(languageAllSites.listSH[lang.lower()])
            
        return Response(list["en"])