from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_id = models.AutoField
    contact_name = models.CharField(max_length=100)
    contact_email = models.CharField(max_length=100)
    contact_msg = models.CharField(max_length=100)

    def __str__(self):
        return self.contact_name