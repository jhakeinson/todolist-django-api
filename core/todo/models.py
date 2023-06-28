from django.db import models

# create model for todo
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('core_user.User', to_field='email', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
