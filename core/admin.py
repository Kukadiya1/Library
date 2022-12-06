from django.contrib import admin
from .models import signUp_data,addBook,confirm_book,return_book,donate_book

# Register your models here.
admin.site.register(signUp_data)
admin.site.register(addBook)
admin.site.register(confirm_book)
admin.site.register(return_book)
admin.site.register(donate_book)

