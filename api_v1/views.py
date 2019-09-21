from django.shortcuts import render
from .models import Pmdex
from django.db import models
from .serializers import PmdexSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class PmDetail(APIView):
    def get(self, request, id, format=None):
        id = '#' + id.zfill(3)
        try:
            pm = Pmdex.objects.get(pm_id=id)
        except Pmdex.DoesNotExist:
            err = {
                'detail': "DoseNotExit",
            }
            return Response(err, status=status.HTTP_404_NOT_FOUND)
        serializer = PmdexSerializer(pm)
        return Response(serializer.data)
