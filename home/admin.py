from django.contrib import admin


# Register your models here.


# username:admin
# password:admin

from django.contrib import admin
# Register your models here.

from .models import Member, FetchBook


class LibraryUserAdmin(admin.ModelAdmin):

    list_display = ('user','name', 'email', 'age', 'address', 'amount_limit')
    list_filter = ('email',)

admin.site.register(Member, LibraryUserAdmin)



class FetchBookAdmin(admin.ModelAdmin):
    list_display = ('book_id','title', 'publication_date', 'text_reviews_count', 'ratings_count', 'language_code')
    list_filter = ('book_id',)

admin.site.register(FetchBook, FetchBookAdmin)

