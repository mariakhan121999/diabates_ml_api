from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from django.views.decorators.csrf import csrf_exempt

import joblib
import os

base_dir = os.path.dirname(__file__)
