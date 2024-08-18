from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField( max_length=50, unique=True, blank=True)
    description = models.TextField(max_length=30)
    
    def __str__(self):
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    complited = models.BooleanField(default=False)
    class Meta:
        ordering = ['created_at']
    
    def get_absolute_url(self):
      return reverse("task_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title
    
