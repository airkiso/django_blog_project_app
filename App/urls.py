from .import views
from django.urls import path

urlpatterns=[
    path('', views.home, name="main"),
    
    path('index/',views.PostList.as_view(),name="home"),
    path('post/<slug:slug>/',views.DetailView.as_view(),name="post_detail"),
]