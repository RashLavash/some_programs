from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'tags']
        # exclude = 'поля, которые хотим исключить'
        labels = {
            'title': 'Название публ.'
        }
