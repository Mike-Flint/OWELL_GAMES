
from django.urls import path,register_converter
from . import views
from main.converters import TwoLetterConverter

register_converter(TwoLetterConverter, 'twoletter')

urlpatterns = [
    path('', views.BS , name="BS_Main"),
    path('<twoletter:lang>',views.BS_languageSite , name="BS_MainLang"),
]
