from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """Un tópico sobre el que el usuario está aprendiendo."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Retorna un string en representación del modelo."""
        return self.text

class Entry(models.Model):
    """Algo específicamente aprendido sobre un tópico."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Retorna una sola string representando la entrada."""
        return f"{self.text[:50]}..."
