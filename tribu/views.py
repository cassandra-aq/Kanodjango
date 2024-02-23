from django import forms
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from .forms import KanomienForm
from .models import Kanomien


class KanomienList(ListView):
    model = Kanomien


class KanomienDetail(DetailView):
    model = Kanomien


class KanomienCreate(CreateView):
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
    success_url = reverse_lazy("kanomien_list")

    def get_form(self):
        form = super().get_form()
        form.fields["date_joined"].widget = forms.DateInput(attrs={"type": "date"})
        return form


class KanomienUpdate(UpdateView):
    model = Kanomien
    form_class = KanomienForm
    success_url = reverse_lazy("kanomien_list")


class KanomienDelete(DeleteView):
    model = Kanomien
    success_url = reverse_lazy("kanomien_list")
