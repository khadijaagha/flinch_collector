#this is where we will define all paths for finchcollector app ,


#! to define routes we need to import a path function and our views file:
from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finch/', views.finches_index, name='index'),
    path('finch/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finch/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finch/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finch/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('finch/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    # associate a toy with a finch (M:M)
    path('finch/<int:finch_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    #unassociate a toy with a finch  
    path('finch/<int:finch_id>/cancel_assoc_toy/<int:toy_id>/', views.cancel_assoc_toy, name='cancel_assoc_toy'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),

    
]