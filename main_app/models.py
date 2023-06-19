from django.db import models
from django.urls import reverse



#tuples of tuples
MEALS = (
('B', 'Breakfast'),
('L', 'Lunch'),
('D', 'Dinner')
)

# Create your models here.

class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})


class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed= models.CharField(max_length=100)
    description= models.TextField(max_length=250)
    age= models.IntegerField()
      #create a M:M r.ship with Toy, need to use plural name bc its many:many:
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    

    #Feeding model 
class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )

    #create a finch_id FK
    finch = models.ForeignKey(
        Finch,
        on_delete=models.CASCADE
    )


    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
        


