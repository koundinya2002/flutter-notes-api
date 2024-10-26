from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('notes/create/', views.createNote),
    path('notes/', views.getNotes),
    path('notes/<str:pk>/', views.getNoteDetails),
    path('notes/<str:pk>/update/', views.updateNote),
    path('notes/<str:pk>/delete/', views.deleteNote),
]