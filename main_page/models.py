from django.db import models


class films(models.Model):
    GENRE_CHOICE = (
        ('Ужасы','Ужасы'),
        ('Комедия','Комедия'),
        ('Боевик','Боевик')
    )
    image = models.ImageField(upload_to='film/', verbose_name='Заргузите картинку')
    title = models.CharField(max_length=100, verbose_name= 'Укажите название фильма')
    description = models.TextField(verbose_name='Укажите описание к фильму', default='Lorem Ipsum', null=True)
    price = models.FloatField(verbose_name='Укажите цену')
    release_date = models.DateField(verbose_name='Укажите дату выхода')
    genre = models.CharField(max_length=100, choices=GENRE_CHOICE,
                             default='Комедия',
                             verbose_name='Укажите жанр фильма')
    time = models.TimeField(verbose_name='Укажите продолжительность фильма')
    director = models.CharField(max_length=100, verbose_name='Укажите имя режиссера')
    trailer = models.URLField(verbose_name='Вставьте ссылку на трейлер с YouTube')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'

    def __str__(self):
        return f'{self.title}-{self.price}$'
