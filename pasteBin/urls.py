from django.urls import path

from .views import PasteHome, ShowPaste, MyPaste

urlpatterns = [
  path('', PasteHome.as_view(), name="home"),
  path('mypaste', MyPaste.as_view(), name="mypaste"),
  path('paste/<int:pk>/', ShowPaste.as_view(), name="paste")
]
