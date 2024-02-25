"""Define patrones de URL para learning_logs."""

from django.urls import  path

# El punto(.) significa desde el directorio actual.
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Pagina que muestra todos los temas.
    path('topics/', views.topics, name='topics'),
    # Página de detalles para un solo tema.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Página para agregar un nuevo tema.
    path('new_topic/', views.new_topic, name='new_topic'),
    # Página para agregar una nueva entrada.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Página para editar una entrada.
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]
