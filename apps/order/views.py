from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response


class OrderView(APIView):
    def get(self, request):
        return Response({})