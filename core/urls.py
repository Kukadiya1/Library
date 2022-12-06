from django.urls import path
from . import views

urlpatterns = [
    path('',views.signUp),
    path('login/',views.login),
    path('home/',views.home),
    path('landbook/',views.landBook),
    path('confirmation/',views.confirmation),
    path('returnbook/',views.returnbook),
    path('donatebook/',views.donate_view),
]