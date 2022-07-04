from django.urls import path
from cuenta.views import( registro_view, login1, )

app_name = "cuenta"

urlpatterns = [
    path('register', registro_view, name="register"),
    path('login1',login1,name="login1")
]