
from django.urls import path,register_converter
from . import views
from main.converters import TwoLetterConverter

register_converter(TwoLetterConverter, 'twoletter')

urlpatterns = [
    path('', views.SH , name="SH_Main"),
    path('<twoletter:lang>',views.SH_languageSite , name="SH_MainLang"),
]

