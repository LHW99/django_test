from django.contrib import admin

# Register your models here.

# first, import the models from your model file, then call them

from .models import Author, Genre, Book, BookInstance

class BookInline(admin.TabularInline):
  model = Book

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)

# Changing how a model is displayed in the admin interface
# Define the admin class for author
class AuthorAdmin(admin.ModelAdmin):
  list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
  fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
  inlines = [BookInline]
# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# adds associated records at the same time
# i.e. add book instances at same time as book
class BooksInstanceInline(admin.TabularInline):
  model = BookInstance

# change how model is displayed for book
# does the same thing as admin.site.register
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  # can't display genre specifically, since it's a ManyToManyField; needs new string
  list_display = ('title', 'author', 'display_genre')
  inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
  # showing filter options for the admin window
  list_display = ('book', 'status', 'borrower', 'due_back', 'id')
  list_filter = ('status', 'due_back')

  fieldsets = (
    (None, {
      'fields': ('book', 'imprint', 'id')
    }),
    ('Availability', {
      'fields': ('status', 'due_back', 'borrower')
    })
  )

