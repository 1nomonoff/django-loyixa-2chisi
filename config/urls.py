
from django.contrib import admin
from django.urls import path
from shop.views import salom
from todo.views import dastur_page
from category.views import category
from product.views import product
from fintechhub.views import fintech

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',salom),
    path('s/',dastur_page),
    path('c/',category),
    path('p/',product),
    path('f/',fintech)

]
