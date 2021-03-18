from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # function defines a pattern to match against the URL ('books/')
    path('books/', views.BookListView.as_view(), name='books'),
]
