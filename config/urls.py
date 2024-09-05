from django.contrib import admin
from django.urls import path
from sun.views import register, register_action

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", register),
    path("register/action",register_action),
]
