from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # function defines a pattern to match against the URL ('books/')
    path('books/', views.BookListView.as_view(), name='books'),
    # special syntax to capture the specific id of the book that we want to see
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>',
    views.AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path(r'borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]
