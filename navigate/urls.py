# from django.contrib import admin
from django.urls import path
from .views import home,contact,about


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home/',home),
    path('about/',about),
    path('contact/',contact),
]
