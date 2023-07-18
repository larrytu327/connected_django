from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), 
    path('about/', views.About.as_view(), name="about"),
    path('messageboards/', views.MessageBoards.as_view(), name="messageboards"),
    path('login/', views.Login.as_view(), name="login"),
    path('messageboards/new/', views.MessageBoardsCreate.as_view(), name="messageboards_create"),
    path('messageboards/<int:pk>/', views.MessageBoardsDetail.as_view(), name="messageboards_detail"),
    path('messageboards/<int:pk>/update', views.MessageBoardsUpdate.as_view(), name="messageboards_update"),
    path('messageboards/<int:pk>/delete', views.MessageBoardsDelete.as_view(), name="messageboards_delete"),
    path('messageboards/<int:pk>/post/new', views.PostCreate.as_view(), name="post_create"),
]
