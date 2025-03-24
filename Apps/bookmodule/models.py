from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)

mybook = Book(title = 'Continuous Delivery', author = 'J.Humble and D. Farley', edition = 1)
mybook.save()
