from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:superhero_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create_new_superhero'),
    path('edit/<int:superhero_id>/', views.edit, name='edit_existing_superhero'),
    path('delete/<int:superhero_id>/', views.edit, name='delete_existing_superhero')
]
