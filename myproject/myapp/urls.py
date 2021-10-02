from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:superhero_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create_new_superhero'),
    path('edit/<superhero_id>/', views.edit, name='edit_existing_superhero'),
    path('delete/<superhero_id>/', views.delete, name='delete_existing_superhero')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


