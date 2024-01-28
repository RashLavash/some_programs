from django.db import models

class Worker(models.Model):
    __tablename__ = 'worker'

    name = models.CharField(max_length=20, blank=False)
    second_name = models.CharField(max_length=25, blank=False)
    salary = models.IntegerField(default=0)


    def __str__(self):
        return self.second_name
