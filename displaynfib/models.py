from django.db import models

class FibOutput(models.Model):
    number = models.IntegerField()  #this is the input number as provied by the user
    result = models.IntegerField() # this is the result seen in 'Nth Fibonacci Number' text lab
    time_taken = models.CharField(max_length=255) # time consumed to provide output
   
def __str__(self):
    return self.number  #throwing the output
