from django.urls import path
from apps.chatbot.views import ChatbotView
from apps.chatbot import views

app_name = 'chatbot'

urlpatterns = [
    path('llm/', ChatbotView.as_view(), name='chatbot'),
    path('clear/', views.clear_chat, name='clear_chat')
]