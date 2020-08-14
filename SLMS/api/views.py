from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import StreetLight
from api.serializers import StreetLightSerializer

# Create your views here.

