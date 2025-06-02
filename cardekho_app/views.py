from django.shortcuts import render
from .models import carlist
from .serializerfolder.serializers import CarSerializer
from rest_framework.response import  Response
from rest_framework.decorators import api_view
#from django.http import JsonResponse
# Create your views here.

#def Car_list_view(request ):
#    car = carlist.objects.all()
 #   data = {
 #       'car' : list(car.values()),
 #   }
 #   return JsonResponse(data)
#def Car_detail_view(request, pk):
 #   car = carlist.objects.get(pk = pk)
 #   data = {
 #       'name' : car.name,
  #      'description' : car.description,
  #      'active' : car.active,
  #  }
  #  return JsonResponse(data)

@api_view(['GET','POST'])
def Car_list_view(request):
    if request.method == 'GET':
        car = carlist.objects.all()
        serializer = CarSerializer(car, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
@api_view()
def Car_detail_view(request, pk):
    car = carlist.objects.get(pk = pk)
    serializer = CarSerializer(car)
    return Response(serializer.data)

