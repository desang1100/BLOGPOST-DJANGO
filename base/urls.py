from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("contacts/", views.contacts, name="contacts"),
    path("post/<str:pk>", views.getPost, name="post_detail"),
    path("post/<str:pk>/delete", views.deletePost, name="post_delete"),
    path("new_post/", views.createPost, name="create_post"),
    path("post/<str:pk>/edit", views.updatePost, name="update_post"),
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerUser, name="register"),
]
