from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    path('',views.index,name='index'),
    # url(r'(?P<id>\d+)/favourite/$', views.favourite, name='favourite'),
    path('delete/<int:id>', views.delete),    
    # path('favourite/<int:id>', views.favourite, name='favourite'),
    # path('favourites/<int:id>', views.favourite_all, name='favourite_all'),
    
]
