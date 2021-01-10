from .views import EncodeView, DecodeView
from django.urls import path

urlpatterns = [
    path("encode", EncodeView.as_view(), name="encode"),
    path(
        "decode",
        DecodeView.as_view(),
        name="decode",
    ),
]
