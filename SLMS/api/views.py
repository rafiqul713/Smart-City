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

    """
    def post(self,request):
        serializer = StreetLightSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            saved = serializer.save()
        return Response({"success": " '{}' created successfully".format(saved.comment)})

    """


class LIGHT_ON_OFF(APIView):
    def post(self,request,id,status):
        id_list=["dev101","dev201","dev301","dev401"]
        flag=False
        if id in id_list:
            flag=True
        if flag==False:
            return Response("Not a valid device id")
        status=status.upper()
        store={"device_id":id,"light_status":status}
        print("Requested data ",request.data)
        if status=="ON":
            self.light_on(id)
        elif status=="OFF":
            self.light_off(id)
        else:
            print("Wrong API calling")

        serializer = StreetLightSerializer(data=store)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            saved = serializer.save()

        return Response("OK")


    def light_on(self,id):
        print("Light num ",id," turn ON")

    def light_off(self,id):
        print("Light num ",id," turn OFF")
