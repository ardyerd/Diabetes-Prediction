import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render


class DiabetesPrediction(APIView):
    def post(self, request):
        data = request.data
        pregnancies = data['Pregnancies']
        glucose = data['Glucose']
        bloodpressure = data['BloodPressure']
        skinthickness = data['SkinThickness']
        insulin = data['Insulin']
        bmi = data['BMI']
        dpf = data['DiabetesPedigreeFunction']
        age = data['Age']

        # input_data = ([[0.04601433,-0.34096773,1.18359575,-1.28821221,-0.69289057,0.71168975,-0.84827977,-0.27575966]])
        scaler = ApiConfig.data_scale
        test_df = pd.DataFrame({'Pregnancies': [data['Pregnancies']],
                               'Glucose': [data['Glucose']],
                                'BloodPressure': [data['BloodPressure']],
                                'SkinThickness': [data['SkinThickness']],
                                'Insulin': [data['Insulin']],
                                'BMI': [data['BMI']],
                                'DiabetesPedigreeFunction': [data['DiabetesPedigreeFunction']],
                                'Age': [data['Age']],
                                })
        # input_data = np.asarray([pregnancies,glucose,bloodpressure,skinthickness,insulin,bmi,dpf,age])
        print(type(test_df))
        a = np.array(test_df)
        print(a)
        scaled_data = scaler.transform(a)
        print(data)
        lin_model = ApiConfig.model
        prediction = lin_model.predict(scaled_data)

        if prediction == 0:
            response_dict = {"Patient is not Diabetic"}
        else:
            response_dict = {"Patient is Diabetic"}

        return Response(response_dict, status=200)
