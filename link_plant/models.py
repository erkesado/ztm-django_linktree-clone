from django.db import models

# Create your models here.
class Profile(models.Model):
    BG_CHOICES = (
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
    )

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    bg_color = models.CharField(max_length=50, choices=BG_CHOICES)

    def __str__(self) -> str:
        return self.name

class Link(models.Model):
    text = models.CharField(max_length=100)
    url = models.URLField()
    profile = models.ForeignKey(Profile, related_name='links', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.profile.name} | {self.url}'