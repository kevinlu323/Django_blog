from django.urls import path, re_path
from . import views

app_name = "blogger"

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('post/tmp/<int:pk>/', views.tmpDetail, name='tmpDetail'),
    path('post/<int:post_id>/', views.detail, name='detail'),
    path('post/<int:post_id>/submitComment', views.addComment,
         name='addComment'),
    path('tmp', views.tmpDetail, name='tmpDetail'),
]
