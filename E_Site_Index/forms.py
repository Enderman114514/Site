from django import forms
from captcha.fields import CaptchaField

from .models import Comment

class CommentForm(forms.ModelForm):
    captcha = CaptchaField(label="验证码")

    class Meta:
        model = Comment
        fields = ["owner", "content"]
        widgets = {
            'content': forms.Textarea(attrs={'cols': 100, 'id': 'text'}),
        }