from django.db import models

# Create your models here.


class List(models.Model):
    """
    *Creating database schema.
    *we required two filed/column in databse tatble
    *Proccess:
        1. Creating field for todo list task name
        2. Creating field for wheather task is completed or not
        3. Creating method for dispalay name in admin webpage

    """

    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item
