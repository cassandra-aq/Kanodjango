from django.db import models
from django.urls import reverse


class Kanomien(models.Model):

    LANGUAGE_CHOICES = {
        "py": "Python",
        "js": "JavaScript",
        "ts": "TypeScript",
        "jv": "Java",
        "csh": "C#",
        "vb": ".Net",
        "cpp": "C++",
        "go": "Go",
        "rb": "Ruby",
    }

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    date_joined = models.DateField()
    favourite_language = models.CharField(
        choices=LANGUAGE_CHOICES,
        max_length=10,
    )
    sherpa = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="trekkers",
        null=True,
        blank=True,
    )
    picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self) -> str:
        return reverse("kanomien_edit", kwargs={"pk": self.pk})
