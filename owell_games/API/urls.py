
from django.urls import path ,register_converter
from . import views
from main.converters import TwoLetterConverter

register_converter(TwoLetterConverter, 'twoletter')

urlpatterns = [
    path('v1/main/languages/<twoletter:lang>',views.MainAPILanguage.as_view() , name="MainAPILang"),
    path('v1/BS/languages/<twoletter:lang>',views.BS_MainAPILanguage.as_view() , name="BS_MainAPILang"),
    path('v1/SH/languages/<twoletter:lang>',views.SH_MainAPILanguage.as_view() , name="SH_MainAPILang"),
]