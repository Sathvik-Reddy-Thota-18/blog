from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('article/<int:id>/',views.article,name='article'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
]