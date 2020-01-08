from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    path('',views.index,name='search'),
    path('delete/<int:id>/', views.delete),    
    path('booklist',views.booklist,name='booklist'),
    
]
