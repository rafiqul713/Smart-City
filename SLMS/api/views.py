from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import StreetLight
from api.serializers import StreetLightSerializer
from django.http import HttpResponse


class SLMS_API(APIView):
    def get(self,request):
        obj= StreetLight.objects.all()
        serializer= StreetLightSerializer(obj, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = StreetLightSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            saved = serializer.save()
        return Response({"success": " '{}' created successfully".format(saved.comment)})

