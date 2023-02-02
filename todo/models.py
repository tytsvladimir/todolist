from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-id']

    def __str__(self):
        return self.name


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_expiration = models.DateTimeField()
    date_completed = models.DateTimeField(null=True, blank=True)
    is_important = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
        ordering = ['-date_created']

    def __str__(self):
        return self.title
