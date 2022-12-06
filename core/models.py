from django.db import models

# SignUp data manange model
class signUp_data(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.first_name

class addBook(models.Model):
    book_image = models.ImageField(upload_to='images/',max_length=300)
    book_name = models.CharField(max_length=50,primary_key=True)
    author = models.CharField(max_length=50)
    language = models.CharField(max_length=30)
    disc = models.TextField(max_length=500)
    def __str__(self):
        return self.book_name

class confirm_book(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    book = models.CharField(max_length=50,primary_key=True)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.book

class return_book(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    book = models.CharField(max_length=50,primary_key=True)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.book

class donate_book(models.Model):
    book = models.CharField(max_length=50,primary_key=True)
    author = models.CharField(max_length=50)
    language = models.CharField(max_length=30)
    disc = models.TextField(max_length=500)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.book
    
