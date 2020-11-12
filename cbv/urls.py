from django.urls import path
from . import views

app_name = 'cbv'

urlpatterns = [
    path('home', views.index, name='home'),
    path('temp', views.NewTemp.as_view(), name='temp'),
    #path('books/', views.IndexView.as_view(), name='index'),
    path('', views.BookListView.as_view(), name='index'),
    path('g/<str:genre>', views.GenereView.as_view(), name='genre'),
    path('books/<slug:slug>/', views.BookDetailView.as_view(), name='book-detail'),
    path('add/', views.AddBookView.as_view(), name='add'),
]