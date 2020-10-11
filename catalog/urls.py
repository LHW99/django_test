from django.urls import path
from . import views
from django.urls import include
from django.views.generic import RedirectView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.index, name='index'),
  path('books/', views.BookListView.as_view(), name='books'),
  path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
  path('authors/', views.AuthorListView.as_view(), name='authors'),
  path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]

urlpatterns += [
  path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
  path('allbooks/', views.AllLoanedBooksView.as_view(), name='all-borrowed'),
  path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
  path('allbookcopies/', views.AllBookCopies.as_view(), name='all-book-copies'),
]

urlpatterns += [
  path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
  path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
  path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]

urlpatterns += [
  path('book/create/', views.BookCreate.as_view(), name='book_create'),
  path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
  path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
]

urlpatterns += [
  path('bookcopy/create/', views.BookCopyCreate.as_view(), name='book_copy_create'),
  path('bookcopy/<int:pk>/update/', views.BookCopyUpdate.as_view(), name='book_copy_update'),
  path('bookcopy/<int:pk>/delete/', views.BookCopyDelete.as_view(), name='book_copy_delete'),
]