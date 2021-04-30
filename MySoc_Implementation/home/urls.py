from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index , name='home'),
    path('about', views.about , name='about'),
    path('services', views.services , name='services'),
    path('contact', views.contact , name='contact'),
    path('login', views.loginUser , name='login'),
    path('mysoc', views.mysoc , name='mysoc'),
    path('complaint', views.complaint , name='complaint'),
    path('complaintstatus', views.complaintstatus, name='complaintstatus'),
    path('maintainancebill', views.maintainancebill, name='maintainancebill'),
    path('dependents', views.dependents, name='dependents'),
    path('Logout', views.LogoutUser, name='Logout'),
    path('payment', views.payment, name='payment'),
    path('forgotpassword', views.forgotpassword, name='forgotpassword')

    

]