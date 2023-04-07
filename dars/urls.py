from django.urls import path
from.views import Kurs1Page,Kurs2Page,Kurs3Page,Kurs4Page,RegistPage,KompPage,ftfPage,New

urlpatterns = [
        path('kurs1/',Kurs1Page.as_view(),name='kurs1'),
        path('kurs2/',Kurs2Page.as_view(),name='kurs2'),
        path('kurs3/',Kurs3Page.as_view(),name='kurs3'),
        path('kurs4/',Kurs4Page.as_view(),name='kurs4'),
        path('registr/',RegistPage.as_view(),name='registr'),
        path('komp/',KompPage.as_view(),name='komp'),
        path('ftf/',ftfPage.as_view(),name='ftf'),
        path('news/',New,name='news')
]