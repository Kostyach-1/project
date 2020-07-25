from django.db import models


class user(models.Model):
    user_name = models.TextField(max_length=30)
    user_position = models.TextField(max_length=200)
    user_company = models.TextField(max_length=30)
    user_description = models.TextField(max_length=500)
    job_title = models.TextField()
    objects = models.Manager()
