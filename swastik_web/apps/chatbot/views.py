# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.views import View
from apps.chatbot.models import ChatMessage

# from apps.chatbot.gpt_models import model
from django.shortcuts import redirect

# from chatbot import Chatbot


class ChatbotView(View):
    template_name = "chatbot/chat_window.html"

    @method_decorator(csrf_protect)
    def get(self, request):
        # Retrieve previous chat messages from the database
        messages = ChatMessage.objects.all()
        return render(request, self.template_name, {"messages": messages})

    @method_decorator(csrf_protect)
    def post(self, request):
        user_input = request.POST.get("message", "")
        chatbot_response = user_input
        # chatbot_response = model.generate("Once upon a time, ", n_predict=55, new_text_callback=new_text_callback, n_threads=8)
        # Save user input and chatbot response to the database
        ChatMessage.objects.create(from_user=True, text=user_input)
        ChatMessage.objects.create(from_user=False, text=chatbot_response)
        return redirect("chatbot:chatbot")


def clear_chat(request):
    ChatMessage.clear_chat_history()
    return redirect("chatbot:chatbot")
