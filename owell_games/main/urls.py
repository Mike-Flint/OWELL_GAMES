

from django.urls import path ,register_converter
from . import views
from .converters import TwoLetterConverter

register_converter(TwoLetterConverter, 'twoletter')

urlpatterns = [
    path('', views.main , name="Main"),
    path('<twoletter:lang>',views.languageSite ),
    path('api/v1/main/languages/<twoletter:lang>',views.MainAPILanguage.as_view() , name="MainAPILanguage")
]