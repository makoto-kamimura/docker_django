# from accounts.models import CustomUser
from django.db import models

class Chat(models.Model):
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    response = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, **kwargs):
        # データベース内の Chat インスタンス数を確認
        chats = Chat.objects.all()
        if chats.count() >= 3:
            # 古いものから削除
            oldest_chat = chats.order_by('created_at').first()
            oldest_chat.delete()

        # インスタンスを作成
        chat = cls(**kwargs)
        chat.save()
        return chat