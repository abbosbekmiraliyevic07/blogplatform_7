from django.urls import path

from .views import *

urlpatterns = [
    path('', homework, name='main'),
    # path('about/<int:pk>/', about, name="about")
    path("detail/<slug:slug>/", detail, name="detail"),
    path("create/", create, name="create"),
    path("edit/<slug:slug>", edit, name="edit"),
    path('delete/<slug:slug>', delete, name="delete")
]
