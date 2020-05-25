from django.urls import path

from .views import(
    IndexView,
    DetailView,
    CreateView
)

app_name = "items"
urlpatterns=[
    path('',IndexView.as_view(),name="index"),
    path('detail/<int:idItem>', DetailView.as_view(), name="detail"),
    path('create/',CreateView.as_view(),name="create")
]