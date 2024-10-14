from django.db import models
from company.models import Company
from users.models import User
class Job(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    salary=models.PositiveIntegerField(default=35000)
    requirements=models.TextField()
    ideal_candidate=models.TextField()
    is_available=models.BooleanField(default=True)
    def __str__(self):
        return self.title