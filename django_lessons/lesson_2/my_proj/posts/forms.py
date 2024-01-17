from django import forms


class PostForm(forms.Form):
    title = forms.CharField(label='Заголовок', max_length=100)
    text = forms.CharField(label='Текст', widget=forms.Textarea)
    date = forms.DateTimeField(label='ДатаВремя')