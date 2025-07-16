from django.db import models
import string, random

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

class ShortURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, default=generate_code)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    access_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.short_code
