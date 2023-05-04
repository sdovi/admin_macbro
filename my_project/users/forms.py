from .models import Users
from django.forms import ModelForm, TextInput


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['title', 'surname', 'number',]

        widgets = {
            "title": TextInput(attrs={
                'class': 'type-1',
                'placeholder': 'Имя',
                'name': 'name'
            }),
            "surname": TextInput(attrs={
                'class': 'type-1',
                'placeholder': 'Фамилия',
                'name': 'surname'
            }),
            "number": TextInput(attrs={
                'class': 'type-1',
                'placeholder': 'Номер телефона',
                'name': 'phone',
                'type': 'number'
            }),
        }
