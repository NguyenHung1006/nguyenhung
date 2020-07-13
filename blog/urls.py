from django.urls import path
from . import views
from .views import (
    List_ListView, 
    ListDetailView, 
    ListCreateView,
    ListUpdateView,
    ListDeleteView,
)

urlpatterns = [
    #Home
    path('', views.home, name='blog-home'),
    path('<int:id>/', views.detailproject, name='blog-detail_project'),

    #Post    
    path('post/', views.post, name='blog-post'),
    path('post/<int:pk>/', views.detailpost, name='blog-detailpost'),
    
    #List
    path('list/', List_ListView.as_view(), name='blog-list'),
    path('list/<int:pk>/', ListDetailView.as_view(), name='blog-detail_list'),
    path('list/new/', ListCreateView.as_view(), name='blog-new_list'),
    path('list/<int:pk>/update/', ListUpdateView.as_view(), name='blog-update_list'),
    path('list/<int:pk>/delete/', ListDeleteView.as_view(), name='blog-delete_list'),
]
