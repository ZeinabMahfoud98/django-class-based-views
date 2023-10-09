from datetime import timezone
from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to='post-img/')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name= ('Post')
        verbose_name_plural=('Posts')


