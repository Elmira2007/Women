from django.db import models

# Create your models here.
class Women(models.Model):
    title = models.CharField(
        max_length = 255
    )
    content = models.TextField(
        blank = True, null = True
    )
    time_create = models.DateTimeField(
        auto_now_add = True
    )
    time_update = models.DateTimeField(
        auto_now = True
    )
    is_published = models.BooleanField(
        default = True
    )
    # cat =models.FloatField('Category', on_delete=models.PROTECT, null=True)
    cat = models.FloatField('Category', null=True)

    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    name = models.CharField(
        max_length = 255,
        db_index = True
    )
    
    def __str__(self):
        return self.name