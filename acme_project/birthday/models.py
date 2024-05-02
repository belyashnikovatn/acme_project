from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from birthday.validators import real_age


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField('Фамилия', blank=True,
                                 help_text='Необязательное поле',
                                 max_length=20)
    birthday = models.DateField('Дата рождения', validators=(real_age,))
    image = models.ImageField('Фото', upload_to='birthdays_images', blank=True)

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )


class Contest(models.Model):
    title = models.CharField('Название', max_length=20)
    description = models.TextField('Описание')
    price = models.IntegerField('Цена',
                                validators=[
                                    MinValueValidator(10),
                                    MaxValueValidator(100)
                                    ],
                                help_text='Рекомендованная розничная цена')
    comment = models.TextField('Комментарий', blank=True)
