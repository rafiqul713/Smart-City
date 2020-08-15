from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import StreetLight
from api.serializers import StreetLightSerializer
from django.http import HttpResponse


@api_view(['GET', 'POST'])
def light_status(request):
    if request.method == 'GET':
        #print("Request data ",request.method)
        obj = StreetLight.objects.all()
        # serializer= StreetLightSerializer(obj)
        print("Serializer ",obj)
        # return Response(serializer.data)
        return HttpResponse("Testing response")

    elif request.method == 'POST':
        return HttpResponse("Testing response")
        # serializer = StreetLightSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


