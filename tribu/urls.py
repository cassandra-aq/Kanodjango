from django.urls import path
from . import views

urlpatterns = [
    path("", views.KanomienList.as_view(), name="kanomien_list"),
    path("new", views.KanomienCreate.as_view(), name="kanomien_new"),
    path("<int:pk>", views.KanomienDetail.as_view(), name="kanomien_detail"),
    path("<int:pk>/edit", views.KanomienUpdate.as_view(), name="kanomien_edit"),
    path("<int:pk>/delete", views.KanomienDelete.as_view(), name="kanomien_delete"),
]
