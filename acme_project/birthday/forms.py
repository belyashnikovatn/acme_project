from django import forms
from birthday.models import Birthday


class BirthdayForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя', max_length=20)
    last_name = forms.CharField(label='Фамилия', required=False,
                                help_text='Необязательное поле')
    birthday = forms.DateField(label='Дата рождения',
                               widget=forms.DateInput(attrs={'type': 'date'}))


class ContestForm(forms.Form):
    title = forms.CharField(label='Название', max_length=20)
    description = forms.CharField(label='Описание',
                                  widget=forms.Textarea(attrs={'rows': '5'}))
    price = forms.IntegerField(min_value=10, max_value=100, label='Цена',
                               help_text='Рекомендованная розничная цена')
    comment = forms.CharField(required=False, label='Комментарий',
                              widget=forms.Textarea(attrs={'rows': '3'}))
