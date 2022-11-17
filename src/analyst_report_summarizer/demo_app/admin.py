from django.contrib import admin

from .models import Book, BookNumber, Character, Author


# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields = ['title', 'description']
    # list_display = ['title', 'description', 'price']
    list_filter = ['published_date']
    search_fields = ['title', 'description']


@admin.register(BookNumber)
class BookNumberAdmin(admin.ModelAdmin):
    pass


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class CharacterAdmin(admin.ModelAdmin):
    pass
