import os
from django.http import Http404
from django.conf import settings
from django.http import response
from django.shortcuts import render , HttpResponse
from .models import ebook 
from django.db.models.functions import Coalesce

# Create your views here.
def home(request):
    ebooks=ebook.objects.order_by(Coalesce('bookid','bookid').desc())
    
    context={
        'ebooks':ebooks,
    }
    return render(request,"home.html",context)

def download(request,slug):
    downloadbook=ebook.objects.filter(slug=slug).first()
    context={
        "downloadbook":downloadbook
    }
    return render(request,"download.html",context)

def search(request):
    search=request.GET["search"]
    allbookname=ebook.objects.filter(bookname__icontains=search)
    allbookauthor=ebook.objects.filter(bookauthor__icontains=search)
    allbook=allbookname.union(allbookauthor)
    context={
        "allbook":allbook,
        'search':search,
    }
    return render(request,'search.html',context)

def bookdownload(request,path):
    book_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(book_path):
        with open(book_path,'rb') as bk:
            response=HttpResponse(bk.read(),content_type="application/book")
            response['content-Disposition']='inline;filename='+os.path.basename(book_path)
            return response
    raise Http404 