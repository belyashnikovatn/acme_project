from django import forms
from birthday.models import Birthday, Contest


class BirthdayForm(forms.ModelForm):

    class Meta():
        model = Birthday
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
    # first_name = models.CharField('Имя', max_length=20)
    # last_name = models.CharField('Фамилия', blank=True,
    #                              help_text='Необязательное поле',
    #                              max_length=20)
    # birthday = models.DateField('Дата рождения')


class ContestForm(forms.ModelForm):

    class Meta:
        model = Contest
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'cols': '22', 'rows': '5'}),
            'comment': forms.Textarea(attrs={'cols': '22', 'rows': '5'})
        }
    # title = forms.CharField(label='Название', max_length=20)
    # description = forms.CharField(label='Описание',
    #                               widget=forms.Textarea(attrs={'rows': '5'}))
    # price = forms.IntegerField(min_value=10, max_value=100, label='Цена',
    #                            help_text='Рекомендованная розничная цена')
    # comment = forms.CharField(required=False, label='Комментарий',
    #                           widget=forms.Textarea(attrs={'rows': '3'}))
