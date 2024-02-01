from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    movie_name = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=False, null=True)
    desc = models.TextField()
    actor_name = models.CharField(max_length=250)
    release_date = models.DateField()
    img = models.ImageField(upload_to='gallery')
    movie_link = models.URLField(max_length=200)

    def __str__(self):
        return self.movie_name
