from django.urls import path, include
from .views import homepage, flightpage, aboutuspage, contactpage, detailspage, indexpage, INNpage, ToursPage

urlpatterns = [
    path('', homepage.as_view(), name='home'),
    path('flight/', flightpage.as_view(), name='flight'),
    path('inn/', INNpage.as_view(), name='inn'), 
    path('tours/', ToursPage.as_view(), name='tours'),
    path('details/', detailspage.as_view(), name='details'),
    path('index/', indexpage.as_view(), name='index'),
    path('aboutus/', aboutuspage.as_view(), name='aboutus'),
    path('contact/', contactpage.as_view(), name='contact'),
]