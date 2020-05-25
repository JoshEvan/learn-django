from django.urls import path

from .views import(
    IndexView,
    DetailView
)

app_name = "items"
urlpatterns=[
    path('',IndexView.as_view(),name="index"),
    path('detail/<int:idItem>', DetailView.as_view(), name="detail")
]