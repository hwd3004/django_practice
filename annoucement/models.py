from django.db import models


class Annoucement(models.Model):

    file = models.FileField(upload_to='media/')

    class Meta:
        db_table = "annoucement"
