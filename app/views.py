from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.conf import settings
from .models import PDF
from .serializers import PDFSerializer
import os
from rest_framework.generics import RetrieveAPIView
from django.shortcuts import render
from django.views.generic import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "app/index.html")

class PDFDetailView(RetrieveAPIView):
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer

class PDFUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        pdf_serializer = PDFSerializer(data=request.data)
        if pdf_serializer.is_valid():
            pdf_serializer.save()
            download_link = request.build_absolute_uri(pdf_serializer.data['file'])
            return Response({"id": pdf_serializer.data['id'], "download_link": download_link}, status=status.HTTP_201_CREATED)
        else:
            return Response(pdf_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
