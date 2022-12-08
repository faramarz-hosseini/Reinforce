from django.db import models


class Character(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    name = models.CharField(unique=True, max_length=50)
    nickname = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()

    release_date = models.DateField()

    is_killer = models.BooleanField()
    is_survivor = models.BooleanField()

    @classmethod
    def all_killers(cls):
        cls.objects.filter(is_killer=True)

    @classmethod
    def all_survivors(cls):
        cls.objects.filter(is_survivor=True)

    def __str__(self):
        return f"{self.name} ({self.nickname})" if self.nickname else f"{self.name}"


class Perk(models.Model):
    name = models.CharField(max_length=50)
    character = models.ForeignKey("Character", on_delete=models.CASCADE, null=True)
    description = models.TextField()
    is_exhaust = models.BooleanField()
