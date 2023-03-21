from django.urls import path
from . import views

urlpatterns = [
    path('send/', views.register, name='send'),
    path('greet/', views.greet, name=' greet'),
    path('', views.SendListView.as_view(), name='home'),
    path('<int:pk>/',views.SendDetailView.as_view(), name='detail'),
    path('new/', views.SendCreateView.as_view(), name='send_new'),
    path('delete/<int:pk>/', views.SendDeleteView.as_view(), name='delete'),
    path('edit/<int:pk>/', views.SendUpdateView.as_view(), name='edit'),
]
