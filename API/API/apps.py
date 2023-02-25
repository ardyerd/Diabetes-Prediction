import os
import joblib

from django.apps import AppConfig
from django.conf import settings


class ApiConfig(AppConfig):
    #default_auto_field = 'django.db.models.BigAutoField'
    name = 'API'
    SCALE_FILE = os.path.join(settings.DATA_SCALE, "scaler_x.joblib")
    data_scale = joblib.load(SCALE_FILE)
    MODEL_FILE = os.path.join(settings.MODELS, "DiabetesPredictionModel.joblib")
    model = joblib.load(MODEL_FILE)
