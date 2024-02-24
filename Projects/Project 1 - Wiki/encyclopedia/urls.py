from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.entry, name='entry'),
    path("edit_page/<str:title>", views.edit_page, name="edit"),
    path("new_page/", views.new_page, name='new_page'),
    path("search/", views.search, name="search"),
    path("random/", views.random, name="random")
]