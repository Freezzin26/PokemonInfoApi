from django.urls import path, re_path
from .views import PmDetail

urlpatterns = [
    path('pokemon/<slug:id>/', PmDetail.as_view()),
]