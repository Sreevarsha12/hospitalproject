from django.urls import path
from hospitalapp import views

urlpatterns = [
    path('', views.new3, name='new3'),
    path('about/',views.about,name='about'),
    path('doctors/',views.doctors,name='doctors'),
    path('departments/',views.departments,name='departments'),
    path('medicine/',views.medicine,name='medicine'),
    path('contact/',views.contact,name='contact'),
     path('booking/',views.booking,name='booking'),
    path('register/',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),

]