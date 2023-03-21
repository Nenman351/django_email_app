from django.db import models


# Create your models here.

class SendMail(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    receiver = models.EmailField()
    created_at = models.DateField(auto_now_add=True)
    sender = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='sender')

    def __str__(self):
        return self.subject
