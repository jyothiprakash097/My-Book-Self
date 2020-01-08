import requests
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.conf import settings
from .models import Book


def index(request):
    try:
        book_data =[]
        if request.method=="POST":
            if "taskAdd" in request.POST:
                print(list(request.POST.items()))
                title=request.POST["title"]
                icon=request.POST["icon"]
                author=request.POST["author"]
                publishdate=request.POST["publishdate"]
                infoLink=request.POST["infoLink"]
                task=Book(title=title,icon=icon,author=author,publishdate=publishdate,infoLink=infoLink)
                task.save()
                return redirect('/')
        #url = 'https://www.googleapis.com/books/v1/volumes?q={}&key=AIzaSyBN1EB3WWf24C-9OF3I9f8mDGEhZ7WPVY4'
            search_url="https://www.googleapis.com/books/v1/volumes?"
            params = {
                'q' : request.POST['search'],
                'api_key' : settings.MOVIE_DATA_API_KEY,
            }
            response=requests.get(search_url,params)
            print(response)
            data=response.json()["items"]
                
            for book in data:
                if "description" in book['volumeInfo']:
                    description = book['volumeInfo']['description']
                else:
                    description = "Description is not available for this Book!"
                    
                if "publishedDate" in book['volumeInfo']:
                    publishedDate = book['volumeInfo']['publishedDate'][:4]
                else:
                    publishedDate = "publishedDate not available"
                if "authors" in book['volumeInfo']:
                    authors = book['volumeInfo']['authors'][0]
                else:
                    authors = "authors not available"
                if "imageLinks" in book['volumeInfo']:
                    imageLinks = book['volumeInfo']['imageLinks']['thumbnail']
                else:
                    imageLinks = "imageLinks not available"
                if "pageCount" in book['volumeInfo']:
                    pageCount = book['volumeInfo']['pageCount']
                else:
                    pageCount = "???"
                
                book_api= {
                    #'id':book.id,
                    'title': book['volumeInfo']['title'],
                    'icon' : imageLinks,
                    'infoLink' : book['volumeInfo']['infoLink'],
                    'pagecount':pageCount,
                    'publishdate' : publishedDate,
                    'description' :description,
                    'author':author,
                }
                book_data.append(book_api)
                print(book_data)
        context = {'book_data' : book_data}
        return render(request, 'BookApi/book_list.html', context) 
    except:
        return render(request,'BookApi/error.html')
def delete(request, id):
    
    if request.method == 'POST':
        Book.objects.filter(id=id).delete()

    return redirect('/booklist')



def booklist(request):
    book=Book.objects.all()
    context = {
    "book": book
    }
    return render(request,'BookApi/book.html',context)



