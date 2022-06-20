from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import permissions
from .serializers import UserSerializer
# from pydoc import plain
import math
from rest_framework.decorators import api_view
import pandas 
import numpy as np

@api_view(['POST'])
def Index(request):
    
    value = request.data
    # print(value)
    planeDf = pandas.DataFrame(value, columns=value.keys())
    # print(planeDf)
    planeDf['planeCapacity'] = planeDf['plane_id'] * 200

    planeDf['flueConsumption'] = (planeDf['passenger_no'] *0.002) + (np.log(planeDf["plane_id"])*0.80)

    planeDf['totalflytime'] = planeDf['planeCapacity'] / planeDf['flueConsumption']

    Total_Fuel = planeDf['flueConsumption'].sum(axis=0)
    Total_Fly = planeDf['totalflytime'].sum(axis=0)

    respData = {"Total Fuel Consumption per min":Total_Fuel,"Total Fly Time":Total_Fly}
    
    return Response(respData)
   
    