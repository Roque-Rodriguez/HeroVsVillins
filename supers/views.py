from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Super
from .serializers import SuperSerializer
from super_types import *
# Create your views here.


@api_view(['GET', 'POST'])
def supers_list(request):
   if request.method == 'GET':
    supers = Super.objects.all()
    serializer = SuperSerializer(supers, many=True)
    return Response(serializer.data)
   elif request.method == 'POST':
       serializer = SuperSerializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    supers = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(supers)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(supers, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)
    elif request.method == 'DELETE':
        supers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""
 # user/client makes a request for all supers
       # 3 possible paths
       # 1 - get all supers, but send them back in a custom dictionary
       # 2 - query parameter, with a value of "hero", -> only send back heroes
       # 3 - query parameter, with a value of "villian", -> only send back villians
        supers = Super.objects.all()
        supertype = SuperTypes.objects.all()

        super_serializer = SuperSerializer(supers, many=True)
        super_type_serializer = SuperTypesSerializer(supertype, many=True)

        custom_dict = {
            "heroes": super_serializer.data,
            "villians": super_type_serializer.data,  
        }

        
    #        heroes_param = request.query_params.get('2')  #foreign key # 2 is Heroes
     #       villians_param = request.query_params.get('1') #forgein key # 1 is Villians
   
      # for super in Supers:      
    
       # print(super)
       
"""