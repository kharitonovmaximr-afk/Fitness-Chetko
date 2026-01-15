from django.db import models

class GroupChat(models.Model):
    city = models.CharField('Город', max_length=100)
    activity = models.CharField('Род деятельности', max_length=100)
    chat_link = models.URLField('Ссылка на чат')
    group_name = models.CharField('Название группы', max_length=150)

    def str(self):
        return f"{self.group_name} ({self.city} – {self.activity})"

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'