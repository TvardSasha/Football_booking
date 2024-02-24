from django.db import models


class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Place(models.Model):
    sector = models.IntegerField()
    row = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return f'Сектор: {self.sector}, Ряд: {self.row}, Місце: {self.number}'
    
    class Meta:
        unique_together = (('sector', 'row', 'number'),)



class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"Ім'я: {self.user}, Місце: {self.place}, Дата: {self.date}"
