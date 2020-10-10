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
  path('allbooks/', views.AllLoanedBooksView.as_view(), name='all-borrowed')
]