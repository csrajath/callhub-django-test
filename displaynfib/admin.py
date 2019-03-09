from django.contrib import admin
from .models import FibOutput # including the app in the admin pane
admin.site.register(FibOutput)
