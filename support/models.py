import uuid

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(allow_unicode=True)

    def __str__(self):
        return self.name


def generate_ticket_id():
    return str(uuid.uuid4()).split("-")[-1]


class Ticket(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    closed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    ticket_id = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if len(self.ticket_id.strip(" ")) == 0:
            self.ticket_id = generate_ticket_id()

        super(Ticket, self).save(*args, **kwargs)  # Call the real save()

    class Meta:
        ordering = ["-created"]


class Answer(models.Model):
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE, blank=False, null=True)
    content = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
