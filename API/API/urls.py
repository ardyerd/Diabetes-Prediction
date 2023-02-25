from django.urls import path
from .views import DiabetesPrediction

app_name = "API"
urlpatterns = [
    path('weight/', DiabetesPrediction.as_view(), name='diabetes_prediction'),
]