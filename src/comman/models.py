from django.db import models

class BaseModel(models.Model):
    created_at= models.DateTimeField(verbose_name='زمان ایجاد',auto_now_add=True,db_index=True)
    update_at= models.DateTimeField(verbose_name='زمان بروزرسانی',auto_now=True)

    class Meta:
        abstract = True
    def __str__(self):
        return f'object PK is {self.pk} this created at {self.created_at} '
    