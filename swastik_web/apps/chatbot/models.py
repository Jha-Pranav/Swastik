from django.db import models


class ChatMessage(models.Model):
    from_user = models.BooleanField()
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.timestamp} {"User" if self.from_user else "Chatbot"}: {self.text}'
    
    @classmethod
    def clear_chat_history(cls):
        cls.objects.all().delete()
