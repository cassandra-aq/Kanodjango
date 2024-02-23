from django.contrib import admin
from .models import Kanomien


@admin.register(Kanomien)
class KanomienAdmin(admin.ModelAdmin):
    list_filter = ["favourite_language", "sherpa"]
