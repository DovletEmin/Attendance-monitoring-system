from django.db import models

class UserCreation(models.Model):
    user_id = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    user_updated_date = models.DateField()
    user_updated_time = models.TimeField()

    def __str__(self):
        return f"{self.user_id} - {self.user_name} - {self.user_updated_date} - {self.user_updated_time}"
    


