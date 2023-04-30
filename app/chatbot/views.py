import logging

from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import My_chat_botForm
from .models import Chat
from django.views.generic import FormView
from django.core import serializers
from .my_chat_bot import MyChatBot

logger = logging.getLogger(__name__)

#my_chat_bot
class My_chat_botView(LoginRequiredMixin, FormView):
    template_name = "my_chat_bot.html"
    form_class = My_chat_botForm
    success_url = '/chatbot/'

    def form_valid(self, form):
        # ユーザーのチャットを取得する
        chats = Chat.objects.filter(user=self.request.user).order_by('created_at')

        # チャットが3つ以上なら最古のものを削除する
        if len(chats) >= 3:
            chats[0].delete()

        message = form.send_message()
        response = MyChatBot("AI：", message)
        chat = Chat(user=self.request.user, message=message, response=response)
        chat.save()
        data = serializers.serialize('json', [chat])
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid form")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chats'] = Chat.objects.filter(user=self.request.user)
        return context