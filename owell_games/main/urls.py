

from django.urls import path ,register_converter
from . import views
from .converters import TwoLetterConverter

register_converter(TwoLetterConverter, 'twoletter')

urlpatterns = [
    path('<twoletter:lang>',views.languageSite , name="MainLang"),
    path('', views.main , name="Main"),
]