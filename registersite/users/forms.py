from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            'name': '名前',
            'birthday': '生年月日',
            'gender': '性別',
        }
        help_texts = {
            'name': '',
            'birthday': '',
            'gender': '',
        }
