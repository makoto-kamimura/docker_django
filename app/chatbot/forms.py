import os

from django import forms

class My_chat_botForm(forms.Form):
    message = forms.CharField(label='メッセージ', max_length=50)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージをここに入力してください。'

    def send_message(self):
        message = self.cleaned_data['message']
        return message