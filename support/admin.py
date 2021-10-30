from django.contrib import admin
from .models import Ticket, Category, Answer

admin.site.register(Ticket)
admin.site.register(Category)
admin.site.register(Answer)
