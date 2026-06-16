
from django.contrib import admin
from django.urls import path
from shop.views import salom

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',salom),
]
