from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("pasteBin.urls")),
    path('user/', include("user_management.urls")),
]
