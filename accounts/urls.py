from django.urls import path

from accounts.views import UserLoginView

urlpatterns = [
    path("login/", UserLoginView.as_view()),
]

app_name = "accounts"
