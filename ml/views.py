from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from django.views.decorators.csrf import csrf_exempt

import joblib
import os

base_dir = os.path.dirname(__file__)


# Create your views here.
@csrf_exempt
@api_view(['POST'])
def predict(request, model_name):
    data = [request.data["input"]]

    load_model = joblib.load(open(base_dir + "/saved_models/" + model_name + ".joblib", 'rb'))
    y_pred = load_model.predict(data)
    return JsonResponse(y_pred[0], safe=False)