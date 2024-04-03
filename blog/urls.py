from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('post/', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail')
]
