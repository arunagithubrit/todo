from django.db import models


# Create your models here.
class Todos(models.Model):
    title=models.CharField(max_length=200)
    user=models.CharField(max_length=200)
    status=models.BooleanField(default=False)
    created_date=models.DateTimeField(null=True,auto_now_add=True)
    due_date=models.DateField(null=True)

    def __str__(self):
        return self.title
    

    
        
    
        