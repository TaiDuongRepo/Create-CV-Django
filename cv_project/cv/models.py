from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Person(models.Model):
    username = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    website = models.URLField()
    github = models.URLField()
    linkedin = models.URLField()
    facebook = models.URLField()

    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("detail", args=[self.id])
    
class Skills(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)
    level = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(0)]
    )

    def __str__(self):
        return self.skill
    