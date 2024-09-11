from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import fields
from rest_framework import serializers
from .models import Candidate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from . import extract

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('firstname', 'email', 'mobile_number')

@api_view(['POST'])
def extract_info(request):
    if 'file' not in request.FILES:
        return Response({"error":"File Not found"},status=status.HTTP_406_NOT_ACCEPTABLE)
    resume_file = request.FILES['file']
    fullfilename = resume_file.name
    filename,extension = fullfilename.split('.')
    print(extension)
    if extension != 'pdf' and extension != 'docx' and extension != 'txt':
        return Response({"Error":"Cant allow this file type"},status=status.HTTP_406_NOT_ACCEPTABLE)
    extracted_data = extract.parse_resume(resume_file,extension)
    print(extracted_data)
    serializer = CandidateSerializer(data=extracted_data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_info(request):
    candidates = Candidate.objects.all()
    serializer = CandidateSerializer(candidates, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)