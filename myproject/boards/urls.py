from django.urls import path

from .views import index, board_topics

urlpatterns = [
    path('', index, name='home'),
    path('boards/<int:pk>/', board_topics, name='board_topics')
]
