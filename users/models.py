from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, )
    age = models.PositiveIntegerField(default=18, validators=[MinValueValidator(5), MaxValueValidator(90)])
    health_group = models.CharField(max_length=50,
                                    choices=[('', '--выберите группу--'),
                                             ('g1', 'I-я группа'),
                                             ('g2', 'II-я группа'),
                                             ('g3', 'III-я группа'),
                                             ('g4', 'IV-я группа'),
                                             ('g5', 'V-я группа'),
                                             ],
                                    default=''
                                    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username