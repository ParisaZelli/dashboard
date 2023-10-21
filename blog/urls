from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path('',views.blog,name='blog'),
    path('<int:num>/',views.blog_details,name='blog_details'),
    path('elements/',views.elements,name='elements'),
    path('latest_news/',views.latest_news,name='latest_news'),
    path('author/<str:auth>/',views.blog,name='author'),
    path('category/<str:cat>/',views.blog,name='category'),
    path('tag/<str:tag_name>/',views.blog,name='Tag'),
    path('search/',views.search,name='search'),
    path('form/',views.test_form,name='form'),
]
