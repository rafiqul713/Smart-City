from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from ws_api.models import WeatherStation
from ws_api.serializers import WeatherStationSerializer
from django.http import HttpResponse
from ws_api.sensors import Sensor

# Create your views here.

class SensorMeasurement(APIView):
    def get(self,request,id,sensor_type):
        id_list=["temperature","humidity","windspeeddirection","solarradiation","visibilitysensor"]
        flag=False
        measurement_value="None"
        if id in id_list:
            flag=True
        if flag==False:
            return Response("Not a valid device id")
        sensor_type=sensor_type.lower()
        print("Requested data ",request.data)
        if sensor_type=="temperature":
            measurement_value= Sensor.read_temperature(self)
        elif sensor_type=="humidity":
            measurement_value= Sensor.read_humidity(self)
        elif sensor_type=="windspeeddirection":
            measurement_value= Sensor.read_winddirectionchange(self)
        elif sensor_type=="solarradiation":
            measurement_value= Sensor.read_solarradiation(self)
        elif sensor_type=="visibilitysensor":
            measurement_value= Sensor.read_visibility(self)

        return Response(measurement_value)
