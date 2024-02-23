from django import forms

from .models import Kanomien


class KanomienForm(forms.ModelForm):

    class Meta:
        model = Kanomien
        fields = [
            "first_name",
            "last_name",
            "city",
            "date_joined",
            "favourite_language",
            "sherpa",
            "picture",
        ]
        widgets = {
            "date_joined": forms.DateInput(attrs={"type": "date"})
        }
