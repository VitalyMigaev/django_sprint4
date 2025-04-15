from django import forms
from django.contrib.auth import get_user_model

from .models import Comment, Post

User = get_user_model()


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('author',)
        widgets = {
            'pub_date': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'placeholder': 'Выберите дату и время'
                },
                format='%Y-%m-%dT%H:%M'
            )
        }


class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'rows': 4,
                    'cols': 20,
                    'placeholder': 'Введите ваш комментарий здесь...'
                }
            )
        }
