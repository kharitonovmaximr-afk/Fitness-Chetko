from django.db import models


class GTONormativ(models.Model):
    GENDER_CHOICES = [
        ('male', 'Мужской'),
        ('female', 'Женский'),
    ]

    MEDAL_CHOICES = [
        ('bronze', 'Бронза'),
        ('silver', 'Серебро'),
        ('gold', 'Золото'),
    ]

    gender = models.CharField('Пол', max_length=10, choices=GENDER_CHOICES)
    medal = models.CharField('Медаль', max_length=10, choices=MEDAL_CHOICES)
    age_group = models.CharField('Возрастная группа', max_length=50)
    run_100m = models.CharField('Бег 100м', max_length=20, blank=True)
    run_3km = models.CharField('Бег 3км', max_length=20, blank=True)
    pull_ups = models.CharField('Подтягивания', max_length=20, blank=True)
    push_ups = models.CharField('Отжимания', max_length=20, blank=True)
    jump = models.CharField('Прыжок в длину', max_length=20, blank=True)
    press = models.CharField('Пресс', max_length=20, blank=True)
    flexibility = models.CharField('Гибкость', max_length=20, blank=True)

    def str(self):
        return f"{self.get_gender_display()} - {self.get_medal_display()} - {self.age_group}"