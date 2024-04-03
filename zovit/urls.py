from django.urls import path
from zovit import views

app_name = 'zovit'

urlpatterns = [
    path('', views.index, name="home"),
    path('contact/', views.contact, name='contact')
]