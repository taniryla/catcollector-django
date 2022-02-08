from django.db import models
from django.urls import reverse

# Create your models here.

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)


class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})
    # there will be a feeding_set related-managed used to access a given cat


class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0],
    )

    # create a cat_id foreign key colum in the table and it will also provide a way to acces the entire cat object that the feeding belongs to
    cat = models.ForeignKey(
        Cat,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-date']

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_meal_display()} on {self.date}"
