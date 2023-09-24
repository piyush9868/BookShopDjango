from home import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("contact", views.contact, name="contact"),
    path("add-new-book-form", views.addNewBookForm, name="Add new book form"),
    path("add-new-book", views.addNewBook, name="Add new Book"),
    path("all", views.index, name = "allBooks"),
    path("fiction", views.categoryFilterView, name = "fictionCategoryFilter"),
    path("non-fiction", views.categoryFilterView, name = "nonfictionCategoryFilter"),
    path("horror", views.categoryFilterView, name = "horrorCategoryFilter"),
    path("children-books", views.categoryFilterView, name = "childrenbookCategoryFilter"),
    path("thriller", views.categoryFilterView, name = "thrillerCategoryFilter"),
]
