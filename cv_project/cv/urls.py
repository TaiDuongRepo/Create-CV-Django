from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/', views.edit, name='edit'),
    path('home/', views.home, name='home'),
    # path('detail/<int:person_id>/', views.detail, name='detail'),
    path('create/', views.PersonCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.PersonDetailView.as_view(), name='detail'),
    path('update/<int:id>/', views.DataUpdateView.as_view(), name='update'),
]
