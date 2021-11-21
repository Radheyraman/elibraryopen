from django.db import models

# Create your models here.

def book_directory_path(instance,filename):
    return 'book_{0}/{1}'.format(instance.bookname,filename)


class ebook(models.Model):
    bookid=models.AutoField(primary_key=True)
    book=models.FileField(upload_to=book_directory_path)
    bookname=models.CharField(max_length=200)
    bookauthor=models.CharField(max_length=200)
    bookdesc=models.CharField(max_length=1000)
    Thumbnail=models.ImageField(upload_to=book_directory_path, verbose_name="Thumbnail")
    slug=models.SlugField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.bookname

    
    
    
    
