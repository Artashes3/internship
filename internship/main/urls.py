
from django.urls import path
from . views import UsersView,LoginUser,LogoutUser,RegisterUser,UserApi,Posts

urlpatterns = [
    path("get_users", UsersView.as_view()),
    path("login",LoginUser.as_view()),
    path("logout", LogoutUser.as_view()),
    path("user_register",RegisterUser.as_view()),
    path("user",UserApi.as_view()),
    path("post", Posts.as_view())
]

