from django.db import models
from django.utils import timezone

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    upload = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False, blank=True, null=True)
    readTime = models.DateTimeField(blank=True, null=True)
    
    
    # def __str__(self):
    #     return self.title
    
    def save(self, *args, **kwargs):
        if self.read:
            self.readTime = timezone.now()
        super(Book, self).save(*args, **kwargs)


# {
#     'id': '',
#     'title': 'GK Bangla',
#     'author': 'Gass',
#     'upload': 
# }

# {
#     'id': '',
#     'title': '',
#     'author': '',
#     'upload': '',
#     'read': '',
#     'readTime': ''
# }