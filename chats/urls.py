from django.urls import path
from chats.views import list_chats, show_chat, create_chat

urlpatterns = [
    path('', list_chats, name='list_chats'),
    path('<int:chat_id>/', show_chat, name='show_chat'),
    path('add/', create_chat, name='create_chat'),
]
