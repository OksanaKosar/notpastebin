
from django.urls import path

from . import views
from .views import CreatePaste, PasteHome, ShowPaste, RegisterUser, LoginUser, logout_user, MyPaste

urlpatterns = [
  path('', PasteHome.as_view(), name="home"),
  path('mypaste', MyPaste.as_view(), name="mypaste"),
  path('addpaste/', CreatePaste.as_view(), name="homepage"),
  path('paste/<int:pk>/', ShowPaste.as_view(), name="paste"),
  path('register/', RegisterUser.as_view(), name="register"),
  path('login/', LoginUser.as_view(), name="login"),
  path('logout/', logout_user, name="logout"),

]