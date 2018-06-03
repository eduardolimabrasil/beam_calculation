from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Calculation
from .serializer import CalculationSerializer


# Create your views here.
class BeamCalculationView(viewsets.GenericViewSet):
    serializer_class = CalculationSerializer
    queryset = Calculation.objects.all()

    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():            
            return Response(serializer.resistance_module(data),status.HTTP_200_OK)
        return Response(serializer.erros, status.HTTP_500_INTERNAL_SERVER_ERROR)


